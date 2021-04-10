from src.experiments import *
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Disabling CPP output information. Comment to see the outputs.
EXECUTE_ON_GPU = True


# Running each experiment for 300 epochs (normally) and 1000 epochs (extended versions)
def epochs(network): return 1000 if network.endswith('extended') else 300


if __name__ == '__main__':
    experiments = [
        CnnLevel1,
        CnnLevel2,
        CnnLevel3,
        CnnLevel4,
        CnnLevel5,
        BlstmLevel1,
        BlstmLevel1Extended,
        BlstmLevel2,
        BlstmLevel2Extended,
        BlstmLevel3,
        BlstmLevel3Extended,
        BlstmLevel4,
        BlstmLevel4Extended,
        BlstmLevel5,
        BlstmLevel5Extended
    ]

    for experiment in experiments:
        with tf.device('/gpu:0' if EXECUTE_ON_GPU else '/cpu:0'):
            model = experiment()
            network_name = model.get_network_name()
            print(f'Running {network_name}.')
            model.fit(epochs=epochs(network_name))
