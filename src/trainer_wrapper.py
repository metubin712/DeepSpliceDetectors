import tensorflow as tf
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.callbacks import TensorBoard
from data_generator import DataGenerator


class TrainerWrapper:
    def __init__(self, name):
        """
        Initializing Some Defaults and taking in variables
        """
        self._model = None
        self._is_summary_shown = False
        self._network_name = name
    
    def _load_data(self, seed):
        data_generator = DataGenerator(seed=seed, upsampling=20, validation_split=0.2)
        self._validation_X, self._validation_y = data_generator.get_validation_data()
        self._training_generator = data_generator.get_training_generator(2000)
        
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
            metrics=['accuracy']
        )
    
    def _fit(self, epochs):
        """
        Calling the fit function
        """
        self._model.fit(
            self._training_generator,
            epochs=epochs,
            shuffle=True,
            validation_data=(self._validation_X, self._validation_y),
            verbose=False,
            callbacks=[
                TensorBoard(
                    log_dir=f'logs/{self._name}',
                    write_graph=False,
                    write_images=False,
                    update_freq="epoch"
                )
            ]
        )
        
    def fit(self, experiments=5, epochs=10):
        for seed in range(experiments):
            self._name = f'{self._network_name}/e{seed}/'
            self._load_data(seed=seed)
            self._create_network()
            self._compile_model()
            if not self._is_summary_shown:
                self._model.summary()
                self._is_summary_shown = True
            self._fit(epochs)
            tf.keras.backend.clear_session()
