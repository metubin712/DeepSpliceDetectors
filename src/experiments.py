from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv1D, Dense, Input, MaxPool1D, Flatten, LSTM, Concatenate
from tensorflow.keras.backend import reverse
from src.trainer_wrapper import TrainerWrapper


class CnnLevel1(TrainerWrapper):
    def __init__(self):
        super(CnnLevel1, self).__init__(name='cnn_level_1')

    def _create_network(self):
        """
        Group: CNN
        Level: 1
        """
        inputs = Input(shape=(140, 4))
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(inputs)
        max_pooled = MaxPool1D(pool_size=7)(conv)
        flatten = Flatten()(max_pooled)
        classifier = Dense(units=5, activation='relu')(flatten)
        outputs = Dense(units=3, activation='softmax')(classifier)
        self._model = Model(inputs=inputs, outputs=outputs)


class CnnLevel2(TrainerWrapper):
    def __init__(self):
        super(CnnLevel2, self).__init__(name='cnn_level_2')

    def _create_network(self):
        """
        Group: CNN
        Level: 2
        """
        inputs = Input(shape=(140, 4))
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(inputs)
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(conv)
        max_pooled = MaxPool1D(pool_size=7)(conv)
        flatten = Flatten()(max_pooled)
        classifier = Dense(units=5, activation='relu')(flatten)
        outputs = Dense(units=3, activation='softmax')(classifier)
        self._model = Model(inputs=inputs, outputs=outputs)


class CnnLevel3(TrainerWrapper):
    def __init__(self):
        super(CnnLevel3, self).__init__(name='cnn_level_3')

    def _create_network(self):
        """
        Group: CNN
        Level: 3
        """
        inputs = Input(shape=(140, 4))
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(inputs)
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(conv)
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(conv)
        max_pooled = MaxPool1D(pool_size=7)(conv)
        flatten = Flatten()(max_pooled)
        classifier = Dense(units=5, activation='relu')(flatten)
        outputs = Dense(units=3, activation='softmax')(classifier)
        self._model = Model(inputs=inputs, outputs=outputs)


class CnnLevel4(TrainerWrapper):
    def __init__(self):
        super(CnnLevel4, self).__init__(name='cnn_level_4')

    def _create_network(self):
        """
        Group: CNN
        Level: 4
        """
        inputs = Input(shape=(140, 4))
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(inputs)
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(conv)
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(conv)
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(conv)
        max_pooled = MaxPool1D(pool_size=7)(conv)
        flatten = Flatten()(max_pooled)
        classifier = Dense(units=5, activation='relu')(flatten)
        outputs = Dense(units=3, activation='softmax')(classifier)
        self._model = Model(inputs=inputs, outputs=outputs)


class CnnLevel5(TrainerWrapper):
    def __init__(self):
        super(CnnLevel5, self).__init__(name='cnn_level_5')

    def _create_network(self):
        """
        Group: CNN
        Level: 5
        """
        inputs = Input(shape=(140, 4))
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(inputs)
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(conv)
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(conv)
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(conv)
        conv = Conv1D(filters=4, kernel_size=3, strides=1, padding='same', activation='relu')(conv)
        max_pooled = MaxPool1D(pool_size=7)(conv)
        flatten = Flatten()(max_pooled)
        classifier = Dense(units=5, activation='relu')(flatten)
        outputs = Dense(units=3, activation='softmax')(classifier)
        self._model = Model(inputs=inputs, outputs=outputs)


class BlstmLevel1(TrainerWrapper):
    def __init__(self):
        super(BlstmLevel1, self).__init__(name='blstm_level_1')

    def _create_network(self):
        """
        Group: BLSTM
        Level: 1
        """
        inputs = Input(shape=(140, 4))

        lstm = LSTM(2, return_sequences=True)(inputs)
        rev_inputs = reverse(inputs, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)

        blstm = Concatenate(axis=-1)([lstm, rev_lstm])

        max_pooled = MaxPool1D(pool_size=7)(blstm)
        flatten = Flatten()(max_pooled)
        classifier = Dense(units=5, activation='relu')(flatten)
        outputs = Dense(units=3, activation='softmax')(classifier)
        self._model = Model(inputs=inputs, outputs=outputs)


class BlstmLevel2(TrainerWrapper):
    def __init__(self):
        super(BlstmLevel2, self).__init__(name='blstm_level_2')

    def _create_network(self):
        """
        Group: BLSTM
        Level: 2
        """
        inputs = Input(shape=(140, 4))

        lstm = LSTM(2, return_sequences=True)(inputs)
        rev_inputs = reverse(inputs, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)

        blstm = Concatenate(axis=-1)([lstm, rev_lstm])

        lstm = LSTM(2, return_sequences=True)(blstm)
        rev_inputs = reverse(blstm, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)

        blstm = Concatenate(axis=-1)([lstm, rev_lstm])

        max_pooled = MaxPool1D(pool_size=7)(blstm)
        flatten = Flatten()(max_pooled)
        classifier = Dense(units=5, activation='relu')(flatten)
        outputs = Dense(units=3, activation='softmax')(classifier)
        self._model = Model(inputs=inputs, outputs=outputs)

class BlstmLevel3(TrainerWrapper):
    def __init__(self):
        super(BlstmLevel3, self).__init__(name='blstm_level_3')

    def _create_network(self):
        """
        Group: BLSTM
        Level: 3
        """
        inputs = Input(shape=(140, 4))
        
        lstm = LSTM(2, return_sequences=True)(inputs)
        rev_inputs = reverse(inputs, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)
        
        blstm = Concatenate(axis=-1)([lstm, rev_lstm])
        
        lstm = LSTM(2, return_sequences=True)(blstm)
        rev_inputs = reverse(blstm, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)
        
        blstm = Concatenate(axis=-1)([lstm, rev_lstm])
        
        lstm = LSTM(2, return_sequences=True)(blstm)
        rev_inputs = reverse(blstm, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)
        
        blstm = Concatenate(axis=-1)([lstm, rev_lstm])
        
        max_pooled = MaxPool1D(pool_size=7)(blstm)
        flatten = Flatten()(max_pooled)
        classifier = Dense(units=5, activation='relu')(flatten)
        outputs = Dense(units=3, activation='softmax')(classifier)
        self._model = Model(inputs=inputs, outputs=outputs)


class BlstmLevel4(TrainerWrapper):
    def __init__(self):
        super(BlstmLevel4, self).__init__(name='blstm_level_4')

    def _create_network(self):
        """
        Group: BLSTM
        Level: 4
        """
        inputs = Input(shape=(140, 4))
        
        lstm = LSTM(2, return_sequences=True)(inputs)
        rev_inputs = reverse(inputs, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)
        
        blstm = Concatenate(axis=-1)([lstm, rev_lstm])
        
        lstm = LSTM(2, return_sequences=True)(blstm)
        rev_inputs = reverse(blstm, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)
        
        blstm = Concatenate(axis=-1)([lstm, rev_lstm])
        
        lstm = LSTM(2, return_sequences=True)(blstm)
        rev_inputs = reverse(blstm, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)
        
        blstm = Concatenate(axis=-1)([lstm, rev_lstm])
        
        lstm = LSTM(2, return_sequences=True)(blstm)
        rev_inputs = reverse(blstm, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)
        
        blstm = Concatenate(axis=-1)([lstm, rev_lstm])
        
        max_pooled = MaxPool1D(pool_size=7)(blstm)
        flatten = Flatten()(max_pooled)
        classifier = Dense(units=5, activation='relu')(flatten)
        outputs = Dense(units=3, activation='softmax')(classifier)
        self._model = Model(inputs=inputs, outputs=outputs)


class BlstmLevel5(TrainerWrapper):
    def __init__(self):
        super(BlstmLevel5, self).__init__(name='blstm_level_5')

    def _create_network(self):
        """
        Group: BLSTM
        Level: 5
        """
        inputs = Input(shape=(140, 4))
        
        lstm = LSTM(2, return_sequences=True)(inputs)
        rev_inputs = reverse(inputs, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)
        
        blstm = Concatenate(axis=-1)([lstm, rev_lstm])
        
        lstm = LSTM(2, return_sequences=True)(blstm)
        rev_inputs = reverse(blstm, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)
        
        blstm = Concatenate(axis=-1)([lstm, rev_lstm])
        
        lstm = LSTM(2, return_sequences=True)(blstm)
        rev_inputs = reverse(blstm, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)
        
        blstm = Concatenate(axis=-1)([lstm, rev_lstm])
        
        lstm = LSTM(2, return_sequences=True)(blstm)
        rev_inputs = reverse(blstm, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)
        
        blstm = Concatenate(axis=-1)([lstm, rev_lstm])
        
        lstm = LSTM(2, return_sequences=True)(blstm)
        rev_inputs = reverse(blstm, axes=1)
        rev_lstm = LSTM(2, return_sequences=True)(rev_inputs)
        
        blstm = Concatenate(axis=-1)([lstm, rev_lstm])
        
        max_pooled = MaxPool1D(pool_size=7)(blstm)
        flatten = Flatten()(max_pooled)
        classifier = Dense(units=5, activation='relu')(flatten)
        outputs = Dense(units=3, activation='softmax')(classifier)
        self._model = Model(inputs=inputs, outputs=outputs)


class BlstmLevel1Extended(BlstmLevel1):
    def __init__(self):
        super(BlstmLevel1Extended, self).__init__()
        self._network_name = 'blstm_level_1_extended'
        self.is_extended = True


class BlstmLevel2Extended(BlstmLevel2):
    def __init__(self):
        super(BlstmLevel2Extended, self).__init__()
        self._network_name = 'blstm_level_2_extended'


class BlstmLevel3Extended(BlstmLevel3):
    def __init__(self):
        super(BlstmLevel3Extended, self).__init__()
        self._network_name = 'blstm_level_3_extended'


class BlstmLevel4Extended(BlstmLevel4):
    def __init__(self):
        super(BlstmLevel4Extended, self).__init__()
        self._network_name = 'blstm_level_4_extended'


class BlstmLevel5Extended(BlstmLevel5):
    def __init__(self):
        super(BlstmLevel5Extended, self).__init__()
        self._network_name = 'blstm_level_5_extended'
