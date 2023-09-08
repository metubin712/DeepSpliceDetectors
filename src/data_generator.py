import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from os.path import expanduser
from tensorflow.keras.utils import Sequence
import math
from sklearn.model_selection import KFold

HOME = expanduser("~")


class TrainingSequence(Sequence):
    def __init__(self, x_set, y_set, batch_size):
        self._x, self._y = x_set, y_set
        self._batch_size = batch_size

    def __len__(self):
        return math.ceil(self._x.shape[0] / self._batch_size)

    def __getitem__(self, idx):
        batch_x = self._x[idx * self._batch_size:(idx + 1) * self._batch_size]
        batch_y = self._y[idx * self._batch_size:(idx + 1) * self._batch_size]

        return np.array(batch_x), np.array(batch_y)


class DataGenerator:
    _data_location = f'{HOME}/.DeepSpliceDetectors'
    
    # Fixed Properties
    _data_files = [
        'EI_true',
        'IE_true',
        'EI_false',
        'IE_false'
    ]
    _EI_true_length = 2796
    _IE_true_length = 2880
    _false_length = 271926 + 329359
    _minority_class_length = min(_EI_true_length, _IE_true_length)
    
    def __init__(self, seed=0, dataset='hs3d', upsampling_minority=1, balancing=True, validation_split=0.2):
        # Seed value for reproducibility of random processes
        self._seed = seed
        self._dataset = dataset
        self._upsampling = upsampling_minority
        self._balancing = balancing
        np.random.rand(seed)
        # Validation split's default value
        self._validation_split = validation_split
        # Loading the data
        self._data = {}
        self._validation = {'X': {}, 'y': {}}
        self._training_org = {'X': {}, 'y': {}}
        self._training = {'X': {}, 'y': {}}
        self._load_files()
        self._combine_falses()
        self._split_data()
        
        # OneHotEncoder Object
        self._X_enc = OneHotEncoder(categories=[[0.0, 1.0, 2.0, 3.0]], handle_unknown='ignore')
        self._y_enc = OneHotEncoder(categories=[[0.0, 1.0, 2.0]], handle_unknown='ignore')
        self._encode_data()
        
        # Validations do not need anymore processing. They will be combined.
        self._combine_validation()
        
    def _load_files(self):
        """
        Loading files into the `self._data` container
        """
        for file_name in self._data_files:
            file = np.load(f'{self._data_location}/{self._dataset}/{file_name}.npz')
            self._data[file_name] = {
                'X': file['X'],
                'y': file['y']
            }
    
    def _combine_falses(self):
        falses = [category for category in self._data if category.endswith('false')]
        false_X_data = [self._data[item]['X'] for item in falses]
        false_y_data = [self._data[item]['y'] for item in falses]
        self._data['false'] = {
            'X': np.concatenate(false_X_data, axis=0),
            'y': np.concatenate(false_y_data, axis=0)
        }
        for item in falses:
            del self._data[item]

    def _split_data(self):
        """
        Prepare the test and validation split.
        """
        validation_size = (int)(self._validation_split * self._minority_class_length)
        for category in self._data.keys():
            X_train, X_val, y_train, y_val = train_test_split(
                self._data[category]['X'],
                self._data[category]['y'],
                test_size=validation_size,
                random_state=self._seed
            )
            self._training_org['X'][category] = X_train
            self._training_org['y'][category] = y_train
            self._validation['X'][category] = X_val
            self._validation['y'][category] = y_val

    def _encode_data(self):
        """
        Onehot encode the data
        """
        for category in self._data.keys():
            self._training_org['X'][category] = self._encode_X(self._training_org['X'][category])
            self._training_org['y'][category] = self._encode_y(self._training_org['y'][category])
            self._validation['X'][category] = self._encode_X(self._validation['X'][category])
            self._validation['y'][category] = self._encode_y(self._validation['y'][category])

    def _encode_X(self, arr):
        return np.reshape(
            self._X_enc.fit_transform(arr.reshape((-1, 1))).toarray(), (-1, 140, 4)
        ).astype(np.float32, copy=False)

    def _encode_y(self, arr):
        return np.reshape(
            self._y_enc.fit_transform(arr.reshape((-1, 1))).toarray(), (-1, 3)
        ).astype(np.float32, copy=False)

    def _upsample(self):
        for category in self._training_org['X']:
            if category.endswith('false'):
                continue
            self._training['X'][category] = np.repeat(self._training_org['X'][category], self._upsampling, axis=0)
            self._training['y'][category] = np.repeat(self._training_org['y'][category], self._upsampling, axis=0)

    def _downsample(self):
        sum_of_truth = 0
        for category in self._training_org['X']:
            if category.endswith('true'):
                sum_of_truth += self._training_org['X'][category].shape[0]
        for category in self._training_org['X']:
            if category.endswith('true'):
                continue
            x, y = self._unison_shuffled_copies(
                self._training_org['X'][category],
                self._training_org['y'][category]
            )
            self._training['X'][category] = x[0:(sum_of_truth // 2) * self._upsampling]
            self._training['y'][category] = y[0:(sum_of_truth // 2) * self._upsampling]

    def _combine_validation(self):
        X = np.concatenate([self._validation['X'][category] for category in self._validation['X']], axis=0)
        y = np.concatenate([self._validation['y'][category] for category in self._validation['y']], axis=0)
        X, y = self._unison_shuffled_copies(X, y)
        self._validation['X'] = X
        self._validation['y'] = y

    @staticmethod
    def _unison_shuffled_copies(a, b):
        assert len(a) == len(b)
        p = np.random.permutation(len(a))
        return a[p], b[p]

    def _combine_training(self):
        X = np.concatenate([self._training['X'][category] for category in self._training['X']], axis=0)
        y = np.concatenate([self._training['y'][category] for category in self._training['y']], axis=0)
        return self._unison_shuffled_copies(X, y)

    def get_validation_data(self):
        return self._validation['X'], self._validation['y']

    def get_training_generator(self, batch_size):
        if self._upsampling > 1:
            self._upsample()
        else:
            self._training = self._training_org
        if self._balancing:
            self._downsample()
        x, y = self._combine_training()
        return TrainingSequence(x, y, batch_size)


class KFoldDataGenerator:
    _data_location = f'{HOME}/.DeepSpliceDetectors'

    # Fixed Properties
    _data_files = [
        'EI_true',
        'IE_true',
        'EI_false',
        'IE_false'
    ]
    _EI_true_length = 0
    _IE_true_length = 0
    _average_class = (_EI_true_length + _IE_true_length) // 2
    _false_length = 0 + 0
    _minority_class_length = min(_EI_true_length, _IE_true_length)

    def __init__(self, seed=0, folds=10):
        self._seed = seed
        np.random.rand(seed)
        # Loading the data
        self._data = {}
        self._load_files()
        self._combine_falses()
        self._downsample()
        self._combine_data()

        # OneHotEncoder Object
        self._X_enc = OneHotEncoder(categories=[[0.0, 1.0, 2.0, 3.0]], handle_unknown='ignore')
        self._y_enc = OneHotEncoder(categories=[[0.0, 1.0, 2.0]], handle_unknown='ignore')
        self._encode_data()

        self._kf = KFold(n_splits=folds, random_state=self._seed)

        self._data['X'], self._data['y'] = self._unison_shuffled_copies(self._data['X'], self._data['y'])

    def _load_files(self):
        """
        Loading files into the `self._data` container
        """
        for file_name in self._data_files:
            file = np.load(f'{self._data_location}/{file_name}.npz')
            self._data[file_name] = {
                'X': file['X'],
                'y': file['y']
            }

    def _combine_falses(self):
        falses = [category for category in self._data if category.endswith('false')]
        false_X_data = [self._data[item]['X'] for item in falses]
        false_y_data = [self._data[item]['y'] for item in falses]
        self._data['false'] = {
            'X': np.concatenate(false_X_data, axis=0),
            'y': np.concatenate(false_y_data, axis=0)
        }
        for item in falses:
            del self._data[item]

    @staticmethod
    def _unison_shuffled_copies(a, b):
        assert len(a) == len(b)
        p = np.random.permutation(len(a))
        return a[p], b[p]

    def _downsample(self):
        x, y = self._unison_shuffled_copies(
            self._data['false']['X'],
            self._data['false']['y']
        )
        self._data['false']['X'], self._data['false']['y'] = x[0:self._average_class], y[0:self._average_class]

    def _combine_data(self):
        x = [self._data[item]['X'] for item in self._data]
        y = [np.reshape(self._data[item]['y'], newshape=(-1, 1)) for item in self._data]
        self._data = {
            'X': np.concatenate(x, axis=0),
            'y': np.concatenate(y, axis=0)
        }

    def _encode_data(self):
        """
        Onehot encode the data
        """
        self._data['X'] = self._encode_X(self._data['X'])
        self._data['y'] = self._encode_y(self._data['y'])

    def _encode_X(self, arr):
        return np.reshape(
            self._X_enc.fit_transform(arr.reshape((-1, 1))).toarray(), (-1, 140, 4)
        ).astype(np.float32, copy=False)

    def _encode_y(self, arr):
        return np.reshape(
            self._y_enc.fit_transform(arr.reshape((-1, 1))).toarray(), (-1, 3)
        ).astype(np.float32, copy=False)

    def data_generator(self):
        for train_idx, val_idx in self._kf.split(X=self._data['X'], y=self._data['y']):
            yield self._data['X'][train_idx], self._data['y'][train_idx], self._data['X'][val_idx], self._data['y'][
                val_idx]


class HS3DKFoldDataGenerator(KFoldDataGenerator):
    _data_location = f'{HOME}/.DeepSpliceDetectors/hs3d'
    _EI_true_length = 2796
    _IE_true_length = 2880
    _average_class = (_EI_true_length + _IE_true_length) // 2
    _false_length = 271926 + 329359
    _minority_class_length = min(_EI_true_length, _IE_true_length)

class CEKFoldDataGenerator(KFoldDataGenerator):
    _data_location = f'{HOME}/.DeepSpliceDetectors/ce'
    _EI_true_length = 6300
    _IE_true_length = 6300
    _average_class = (_EI_true_length + _IE_true_length) // 2
    _false_length = 173700 + 173700
    _minority_class_length = min(_EI_true_length, _IE_true_length)


if __name__ == "__main__":
    # Creating Data Generator
    k_fold_generator = KFoldDataGenerator(seed=0, folds=10)
    generator = k_fold_generator.data_generator()
    for fold, (x_train, y_train, x_val, y_val) in enumerate(generator):
        print(f'\tFold {fold + 1}')
        print(f'Shape of Training Data: {x_train.shape}')
        print(f'Shape of Training Labels: {y_train.shape}')
        print(f'Shape of Validation Data: {x_val.shape}')
        print(f'Shape of Validation Labels: {y_val.shape}')
        print()
