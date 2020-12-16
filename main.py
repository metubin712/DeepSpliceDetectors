from src.experiments import *
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

if __name__ == '__main__':
    execute_on_gpu = True
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
        with tf.device('/gpu:0' if execute_on_gpu else '/cpu:0'):
            model = experiment()
            network_name = model.get_network_name()
            print(f'Running {network_name}.')
            model.fit(experiments=10, epochs=1000 if network_name.endswith('extended') else 300)
