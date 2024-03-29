# Deep Splice Detectors

This repository contains the code for reproducing the experiments in the article "**An automated framework for evaluation of deep learning models for splice site predictions**".

## Reproducing the Experiments

To reproduce the experiments:

1. Make sure the `pip` is up-to-date, and install the requirements:
```shell
pip install --upgrade pip
pip install -r requirements.txt
```

1. Download the necessary data:
```shell
sh download_data.sh
```

1. Run the main function:
```shell
python main.py
```

**Important Note:** The complete run of the experiments (training and evaluating **150 neural networks**) can take a very long time. The experiments for the article have been executed on an **Nvidia GeForce 1080 Ti** and took +72 hours.

### Using GPU for Computation

The experiments will automatically use the available GPU on the system (given that the proper libraries and driver is installed). If you would like to disable the use of GPU, change the `EXECUTE_ON_GPU` variable in the *main* file to `False`.

## Reproducing the Experiments (Docker Version)

Build the image.

```shell
docker build -t deep-splice-detectors .
```

Create a persistent container from the image with name `DeepSpliceDetectors` and start training.

```shell
docker run -it -d --name DeepSpliceDetectors -p 6006:6006 --gpus all deep-splice-detectors python main.py
```

To stop and start the training process, use the following.

```shell
docker start DeepSpliceDetectors
```

```shell
docker stop DeepSpliceDetectors
```

**Note:** To use *GPU* resources within the docker container make sure that the [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-docker) is installed. Without a proper setup, the code will only execute on *CPU*.

## Compatibility and Requirements

- All provided code (including shell scripts to download the data and log files) are tested in **GNU/Linux** and **macOS** operating systems. Complete **Windows** support may not be 100%.

- We recommend using python `3.8.x` for the experiments. Python 2.x is not supported.

- Python package requirements are available at `requirements.txt` file.

## The Result

After a complete execution of the experiments, you can investigate the resulting statistics such as accuracy, computation time, etc. by:

1. Viewing the log files using [Tensorboard](https://www.tensorflow.org/tensorboard)
```shell
tensorboard --host=0.0.0.0 --logdir <path-to-logs>
```

Docker Example:

```shell
$ docker exec -it DeepSpliceDetectors tensorboard --logdir <path-to-logs> --host=0.0.0.0
```

2. Using our [Jupyter Notebook](https://jupyter.org/) to recreate the graphs used in the article.

## Accessing Our Experiment Log Files

For those who are interested in examining the log files and cannot retrain the networks, the following command will download our log files and place them in `logs.hs3d/`, `logs.ce/`, and `logs.nobidir/` directories in project's root.
- `logs.hs3d/` is for experiments with _HS3D_ dataset.
- `logs.ce/` is for experiments with _CE_ dataset.
- `logs.nobidir/` is for experiments with _None-Bidirectional Architectures_.

```shell
sh download_our_logs.sh
```

# Citation

Please use the following bibtex to cite the article or this repository:
```text
@article{zabardast2023automated,
  title={An automated framework for evaluation of deep learning models for splice site predictions},
  author={Zabardast, Amin and Tamer, Elif G{\"u}ney and Son, Ye{\c{s}}im Ayd{\i}n and Y{\i}lmaz, Arif},
  journal={Scientific Reports},
  volume={13},
  number={1},
  pages={10221},
  year={2023},
  publisher={Nature Publishing Group UK London}
}
```

# Contact

For any inquiries about the code in the repository or the article, contact us using [zabardast.amin@metu.edu.tr](mailto:zabardast.amin@metu.edu.tr) or [a.yilmaz@maastrichtuniversity.nl](mailto:a.yilmaz@maastrichtuniversity.nl)