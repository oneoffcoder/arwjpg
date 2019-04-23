# arwjpg

A simple Python 3.6 script that converts RAW files from some Sony cameras (tested with Sony - Alpha a6300 Mirrorless Camera)  to JPG files. The RAW files should have the `ARW` file extension. This project borrowed key ideas from [Python Image Converter](https://github.com/Cyb3rN4u7/Python-Image-Converter). If all else fails, you should use Sony's [Imaging Edge](http://support.d-imaging.sony.co.jp/app/imagingedge/en/). Imaging Edge is a great software and will likely give you superior conversion quality, however, the conversion is rather slow (images are NOT converted in parallel). In any case, `DO NOT` throw away your RAW files just because you have converted them to JPG.

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

Here is the full set of options.

```bash
usage: arwjpg.py [-h] -s SOURCE -t TARGET [-v VERBOSITY] [-e EXTENSION]
                 [--use_camera_wb USE_CAMERA_WB] [--use_auto_wb USE_AUTO_WB]
                 [--bright BRIGHT]
                 [--median_filter_passes MEDIAN_FILTER_PASSES]
                 [--noise_thr NOISE_THR] [--dcb_enhance DCB_ENHANCE]
                 [--four_color_rgb FOUR_COLOR_RGB]
                 [--demosaic_algorithm DEMOSAIC_ALGORITHM]
                 [--fbdd_noise_reduction FBDD_NOISE_REDUCTION]
                 [--output_color OUTPUT_COLOR] [--output_bps OUTPUT_BPS]

Convert ARW to JPG

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        source directory
  -t TARGET, --target TARGET
                        target directory
  -v VERBOSITY, --verbosity VERBOSITY
                        verbosity
  -e EXTENSION, --extension EXTENSION
                        output extension; JPG or TIFF
  --use_camera_wb USE_CAMERA_WB
                        whether to use the as-shot white balance values
  --use_auto_wb USE_AUTO_WB
                        whether to try automatically calculating the white
                        balance
  --bright BRIGHT       brightness scaling
  --median_filter_passes MEDIAN_FILTER_PASSES
                        number of median filter passes after demosaicing to
                        reduce color artifacts
  --noise_thr NOISE_THR
                        threshold for wavelet denoising (default disabled)
  --dcb_enhance DCB_ENHANCE
                        DCB interpolation with enhanced interpolated colors
  --four_color_rgb FOUR_COLOR_RGB
                        whether to use separate interpolations for two green
                        channels
  --demosaic_algorithm DEMOSAIC_ALGORITHM
                        default is AHD; AAHD, AFD, AHD, AMAZE, DCB, DHT,
                        LINEAR, LMMSE, MODIFIED_AHD, PPG, VCD,
                        VCD_MODIFIED_AHD, VNG
  --fbdd_noise_reduction FBDD_NOISE_REDUCTION
                        controls FBDD noise reduction before demosaicing;
                        Full, Light, Off
  --output_color OUTPUT_COLOR
                        output color space; Adobe, ProPhoto, Wide, XYZ, raw,
                        sRGB
  --output_bps OUTPUT_BPS
                        8 or 16
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
