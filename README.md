# Deep Splice Detectors

This repository contains the code for reproducing the experiments in the article "**A Comparative Evaluation of Bidirectional LSTM and Convolutional Networks for Prediction of Splice Sites**".

## Reproducing the Experiments

To reproduce the experiments:

1. Install the requirements:
```shell
$ pip install -r requirements.txt
```

2. Run the main function:
```shell
$ python main.py
```

**Important Note:** The complete run of the experiments can take a very long time. The experiments for the article have been executed on a **Nvidia GeForce 1080 Ti** and took +24 hours.

### Using GPU for Computation

The experiments will automatically use the available GPU on the system (given that the proper libraries and driver is installed). If you would like to disable the use of GPU, change the `EXECUTE_ON_GPU` variable in the *main* file to `False`.

## The Result

After a complete execution of the experiments, you can investigate the resulting statistics such as accuracy, computation time, etc. by either:

1. View the log files using *Tensorboard*
```shell
$ tensorboard --logdir logs/
```

2. Use our *Jupyter Notebook* and recreate the graphs used in the article.

# Citation

Please use the following bibtex to cite the article or this repository:
```text
TODO: Complete the citation
```

# Contact

For any inquiries about the code in the repository or the article, contact us using [zabardast.amin@metu.edu.tr](mailto:zabardast.amin@metu.edu.tr) or [a.yilmaz@maastrichtuniversity.nl](mailto:a.yilmaz@maastrichtuniversity.nl)