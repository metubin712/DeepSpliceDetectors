import tensorflow as tf
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint
from src.data_generator import KFoldDataGenerator
from tensorflow.keras.metrics import AUC, Precision, Recall
from tensorflow_addons.metrics import F1Score
from tensorflow.keras.models import load_model


class TrainerWrapper:
    def __init__(self, name):
        """
        Initializing Some Defaults and taking in variables
        """
        self._model = None
        self._is_summary_shown = False
        self._network_name = name
        self._data_generator = None
        self._batch_size = 200
        self._model_file_location = f'models/{self._network_name}.hdf5'

    def _load_data(self, seed=0):
        data = KFoldDataGenerator(
            seed=seed,
            folds=10
        )
        self._data_generator = data.data_generator()

    def _create_network(self):
        """
        This network here is a simple CNN.
        This function should be filled in with the classes that are derived from this class
        """
        pass

    def _compile_model(self):
        self._model.compile(
            loss=categorical_crossentropy,
            optimizer=SGD(learning_rate=0.01),
            metrics=[
                'accuracy',
                Precision(name='precision'),
                Recall(name='recall'),
                F1Score(num_classes=3, name='f1'),
                AUC(curve='ROC', name='auc_roc'),
                AUC(curve='PR', name='auc_pr'),
            ]
        )

    def _fit(self, train_x, train_y, val_x, val_y, epochs):
        """
        Calling the fit function
        """
        self._model.fit(
            x=train_x,
            y=train_y,
            batch_size=self._batch_size,
            epochs=epochs,
            shuffle=True,
            validation_data=(val_x, val_y),
            verbose=False,
            callbacks=[
                TensorBoard(
                    log_dir=f'logs/{self._name}',
                    write_graph=False,
                    write_images=False,
                    update_freq="epoch"
                ),
                ModelCheckpoint(
                    self._model_file_location,
                    save_best_only=True,
                    monitor='val_auc_pr',
                    save_freq='epoch',
                    mode='max'
                    )
            ]
        )

    def fit(self, epochs=10):
        self._load_data(seed=1990)
        for fold, (train_x, train_y, val_x, val_y) in enumerate(self._data_generator):
            self._name = f'{self._network_name}/e{fold}/'
            self._create_network()
            self._compile_model()
            if not self._is_summary_shown:
                self._model.summary()
                self._is_summary_shown = True
            self._fit(
                train_x=train_x,
                train_y=train_y,
                val_x=val_x,
                val_y=val_y,
                epochs=epochs
            )
            tf.keras.backend.clear_session()

    def get_network_name(self):
        return self._network_name

    def load_from_disk(self):
        try:
            self._model = load_model(self._model_file_location)
        except OSError:
            print('Model Does Not Exist!')

    def evaluate(self, x, y):
        return self._model.evaluate(
            x,
            y,
            batch_size=self._batch_size,
            verbose=False,
            return_dict=True
        )
