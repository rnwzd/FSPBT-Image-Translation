
<h3 align="center">Few Shot Patch Based Training for Image Translation using PyTorch Lightning</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)


</div>

---


![Teaser](doc/webcam.gif)
Trained using NVIDIA GTX 1050 Ti in seven minutes.
Yep, this is me.

## About <a name = "about"></a>

This is my personal implementation of following the paper using PyTorch Lightning.

> **Interactive Video Stylization Using Few-Shot Patch-Based Training** </br>
_[O. Texler](https://ondrejtexler.github.io/), [D. Futschik](https://dcgi.fel.cvut.cz/people/futscdav),
[M. Kučera](https://www.linkedin.com/in/kuceram/), [O. Jamriška](https://dcgi.fel.cvut.cz/people/jamriond), 
[Š. Sochorová](https://dcgi.fel.cvut.cz/people/sochosar), [M. Chai](http://www.mlchai.com), 
[S. Tulyakov](http://www.stulyakov.com), and [D. Sýkora](https://dcgi.fel.cvut.cz/home/sykorad/)_ </br>
[[`WebPage`](https://ondrejtexler.github.io/patch-based_training)],
[[`Paper`](https://ondrejtexler.github.io/res/Texler20-SIG_patch-based_training_main.pdf)],
[[`BiBTeX`](#CitingFewShotPatchBasedTraining)]


I wrote it as an exercise to learn PyTorch.
I tried many different variants of the models but the original one is the one that works the best.

You can find more information on the official github page
https://github.com/OndrejTexler/Few-Shot-Patch-Based-Training

and on the Lightning docs
https://pytorch-lightning.readthedocs.io/en/latest/

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 


### Installing

Tested with Python 3.9, pytorch 1.8.0 on Ubuntu 20.04 using conda

```
conda create -n FSPBT -y
conda activate FSPBT
conda install -y -c pytorch -c conda-forge pytorch torchvision cudatoolkit   pytorch-lightning
```

### Demo data and pretrained models

To download the demo data along with pretrained models (on Linux)
```
./download_data.sh
```

Alternatively you can download it from  https://drive.google.com/file/d/1WI71nYP-z0mfDpuUW36s3sswpwRwwfrN/view
and extract in the "data" folder

### Training

You can just start

```
conda activate FSPBT
python train.py
```
settings for data_path are inside the file itself

Files are expected to be in folders
```
data_path/
          input
          target
          mask (optional)
```
### View logs
The trainer uses default Lightning logger (Tensorboard)

```
conda activate FSPBT
tensorboard --logdir lightning_logs/ 
```

### Evaluation

You can just start

```
conda activate FSPBT
python eval.py
```

Files will be produced in folder "data_path/output", but you can change it in eval.py



## Authors <a name = "authors"></a>

- [Midas Gordiades (Lorenzo Breschi)](https://github.com/rnwzd) - PyTorch Lightning implementation


##  Acknowledgements <a name = "acknowledgement"></a>
All credits go to the original authors

> **Interactive Video Stylization Using Few-Shot Patch-Based Training** </br>
_[O. Texler](https://ondrejtexler.github.io/), [D. Futschik](https://dcgi.fel.cvut.cz/people/futscdav),
[M. Kučera](https://www.linkedin.com/in/kuceram/), [O. Jamriška](https://dcgi.fel.cvut.cz/people/jamriond), 
[Š. Sochorová](https://dcgi.fel.cvut.cz/people/sochosar), [M. Chai](http://www.mlchai.com), 
[S. Tulyakov](http://www.stulyakov.com), and [D. Sýkora](https://dcgi.fel.cvut.cz/home/sykorad/)_ </br>
[[`WebPage`](https://ondrejtexler.github.io/patch-based_training)],
[[`Paper`](https://ondrejtexler.github.io/res/Texler20-SIG_patch-based_training_main.pdf)],
[[`BiBTeX`](#CitingFewShotPatchBasedTraining)]


## <a name="CitingFewShotPatchBasedTraining"></a>Citing
If you find Interactive Video Stylization Using Few-Shot Patch-Based Training useful 
for your research or work, please use the following BibTeX entry.

```
@Article{Texler20-SIG,
    author    = "Ond\v{r}ej Texler and David Futschik and Michal Ku\v{c}era and Ond\v{r}ej Jamri\v{s}ka and \v{S}\'{a}rka Sochorov\'{a} and Menglei Chai and Sergey Tulyakov and Daniel S\'{y}kora",
    title     = "Interactive Video Stylization Using Few-Shot Patch-Based Training",
    journal   = "ACM Transactions on Graphics",
    volume    = "39",
    number    = "4",
    pages     = "73",
    year      = "2020",
}
```