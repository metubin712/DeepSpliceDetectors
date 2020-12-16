from src.experiments import CnnLevel1, CnnLevel2
import tensorflow as tf

if __name__ == '__main__':
    execute_on_gpu = True
    experiments = [CnnLevel1, CnnLevel2]

    for experiment in experiments:
        with tf.device('/gpu:0' if execute_on_gpu else '/cpu:0'):
            model = experiment()
            model.fit(experiments=2, epochs=10)
