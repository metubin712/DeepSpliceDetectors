from src.experiments import *
import tensorflow as tf
import os
from src.data_generator import DataGenerator

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Disabling CPP output information. Comment to see the outputs.
EXECUTE_ON_GPU = True


if __name__ == '__main__':
    experiments = [
        CnnLevel1
    ]

    # Loading the evaluation data
    x, y = DataGenerator().get_validation_data()

    # Evaluating for each model
    for experiment in experiments:
        with tf.device('/gpu:0' if EXECUTE_ON_GPU else '/cpu:0'):
            model = experiment()
            network_name = model.get_network_name()
            print(f'Evaluating {network_name}.')
            model.load_from_disk()
            result = model.evaluate(x, y)
            print(result)
