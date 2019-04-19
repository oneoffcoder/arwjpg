# arwjpg

A simple Python 3.6 script that converts RAW files from Sony camera to JPG files. The RAW files should have the `ARW` file extension. This project borrowed key ideas from [Python Image Converter](https://github.com/Cyb3rN4u7/Python-Image-Converter).

# Conda environment creation

To use `arwjpg`, you should create a [Conda environment](https://anaconda.org/). Clone this repository and change directory `cd` into it. Then type in the following.

```bash
conda env create -f environment.yml
conda activate arwjpg
```

If you need to destroy the environment, type in the following.

```bash
conda remove --name arwjpg --all
```

# Usage

To use the `arwjpg.py` Python script, make sure you activate the `arwjpg` Conda environment as mentioned above. Then type in the following.

```bash
python arwjpg.py -s [source_dir] -t [target_dir]
```

Note that

* `source_dir` is a directory containing `ARW` (RAW) files.
* `target_dir` is the directory which `JPG` (JPEG) files will be placed.

By default, `ALL` your CPUs will be used to convert `ARW` files to `JPG` files! An example on Windows is given as follows.

```bash
python arwjpg.py -s C:/Users/super/Desktop/100MSDCF -t C:/Users/super/Desktop/JPG
```

# Citation

```
@misc{oneoffcoder_arwjpg_2019, 
title={arwjpg}, 
url={https://github.com/oneoffcoder/arwjpg/}, 
journal={GitHub},
author={One-Off Coder}, 
year={2019}, 
month={Apr}}
```

# Copyright Stuff

```
Copyright 2019 One-Off Coder

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
