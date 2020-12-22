# Deep Splice Detectors

This repository contains the code for reproducing the experiments in the article "**A Comparative Evaluation of Bidirectional LSTM and Convolutional Networks for Prediction of Splice Sites**".

## Reproducing the Experiments

To reproduce the experiments:

1. Install the requirements:
```shell
$ pip install -r requirements.txt
```

2. Download the necessary data:
```shell
$ sh download_data.sh
```

2. Run the main function:
```shell
$ python main.py
```

**Important Note:** The complete run of the experiments (training and evaluating **150 neural networks**) can take a very long time. The experiments for the article have been executed on a **Nvidia GeForce 1080 Ti** and took +72 hours.

### Using GPU for Computation

The experiments will automatically use the available GPU on the system (given that the proper libraries and driver is installed). If you would like to disable the use of GPU, change the `EXECUTE_ON_GPU` variable in the *main* file to `False`.

## Compatibility and Requirements

All provided code (including shell scripts to download the data and log files) are tested in **GNU/Linux** and **macOS** operating systems. Complete **Windows** support may not be 100%.

A variety of Python interpreters are tested for code compatibility (from 3.6.0 to 3.8.6). Python 2.x is not supported.

## The Result

After a complete execution of the experiments, you can investigate the resulting statistics such as accuracy, computation time, etc. by either:

1. View the log files using [Tensorboard](https://www.tensorflow.org/tensorboard)
```shell
$ tensorboard --logdir logs/
```

2. Use our [Jupyter Notebook](https://jupyter.org/) and recreate the graphs used in the article.

## Accessing Log Files

For those who are interested in examining the log files and cannot retrain the networks, th following command will download our log files and place them in `logs/` directory in project's root.
```shell
$ sh download_our_logs.sh
```

# Citation

Please use the following bibtex to cite the article or this repository:
```text
TODO: To Be Completed
```

# Contact

For any inquiries about the code in the repository or the article, contact us using [zabardast.amin@metu.edu.tr](mailto:zabardast.amin@metu.edu.tr) or [a.yilmaz@maastrichtuniversity.nl](mailto:a.yilmaz@maastrichtuniversity.nl)