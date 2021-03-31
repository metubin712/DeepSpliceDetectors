from src.experiments import *
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Disabling CPP output information. Comment to see the outputs.
EXPERIMENTS = 10  # Run 10 experiments per each Level of each Group
EXECUTE_ON_GPU = True


if __name__ == '__main__':
    experiments = [
        CnnLevel5,
        CnnLevel5Up5,
        CnnLevel5Up10,
        CnnLevel5Up15,
        CnnLevel5Up20,
        CnnLevel5Up25
    ]

    for experiment in experiments:
        with tf.device('/gpu:0' if EXECUTE_ON_GPU else '/cpu:0'):
            model = experiment()
            network_name = model.get_network_name()
            print(f'Running {network_name}.')
            model.fit(experiments=EXPERIMENTS, epochs=300)
