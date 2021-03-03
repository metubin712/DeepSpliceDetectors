# Deep Splice Detectors

This repository contains the code for reproducing the experiments in the article "**A Comparative Evaluation of Bidirectional LSTM and Convolutional Networks for Prediction of Splice Sites**".

## Reproducing the Experiments

To reproduce the experiments:

1. Make sure the `pip` is up-to-date, and install the requirements:
```shell
$ pip install --upgrade pip
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

## Reproducing the Experiments (Docker Version)

Build the image.

```shell
$ docker build -t deep-splice-detectors .
```

Create a persistent container from the image with name `DeepSpliceDetecors`.

```shell
$ docker run -it -d --name DeepSpliceDetecors --gpus all deep-splice-detectors python main.py
```

To stop and start the training process, use the following.

```shell
$ docker stop DeepSpliceDetectors
$ docker Start DeepSpliceDetectors
```

**Note:** to use *GPU* resources within the docker caontainer make sure that the [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-docker) is installed. Without a proper setup, the code will only execute on *CPU*.

## Compatibility and Requirements

- All provided code (including shell scripts to download the data and log files) are tested in **GNU/Linux** and **macOS** operating systems. Complete **Windows** support may not be 100%.

- We recommand using python 3.8+ for the experiments. Python 2.x is not supported.

- Python package requirements are available at `requirements.txt` file.

## The Result

After a complete execution of the experiments, you can investigate the resulting statistics such as accuracy, computation time, etc. by:

1. Viewing the log files using [Tensorboard](https://www.tensorflow.org/tensorboard)
```shell
$ tensorboard --logdir logs/
```

Docker Example:

```shell
$ docker exec -it -p 6006:6006 DeepSpliceDetectors tensorboard --logdir logs
```

2. Using our [Jupyter Notebook](https://jupyter.org/) to recreate the graphs used in the article.

## Accessing Our Experiment Log Files

For those who are interested in examining the log files and cannot retrain the networks, the following command will download our log files and place them in `logs/` directory in project's root.
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