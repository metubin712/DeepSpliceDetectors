from src.experiments import *
import tensorflow as tf

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
        print(f'Running {experiment.get_network_name()}.')
        with tf.device('/gpu:0' if execute_on_gpu else '/cpu:0'):
            model = experiment()
            model.fit(experiments=2, epochs=10)
