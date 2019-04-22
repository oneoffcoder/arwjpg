import rawpy
import imageio
import argparse
import sys
import os
import PIL
import multiprocessing

from os import listdir
from os.path import isfile, join
from joblib import Parallel, delayed
from tqdm import tqdm



def make_dir(dir_path):
    """
    Make a directory if it does not exists.
    :param dir_path: Directory path.
    :return: None.
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def convert_raw(source, target):
    """
    Converts a ARW file to a JPG file.
    :param source: ARW file path.
    :param target: JPG file path.
    :return: 1 if successful, else 0.
    """
    result = 0
    try:
        with rawpy.imread(source) as raw:
            rgb = raw.postprocess(use_auto_wb=True)
            # imageio.imwrite(target, rgb)
            PIL.Image.fromarray(rgb).save(target, quality=100, optimize=True)
            result = 1	
    except:
        result = 0
    return result


def parse_args(args):
    """
    :param args: Arguments passed to program.
    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Convert ARW to JPG')
    parser.add_argument('-s', '--source', help='source directory', required=True)
    parser.add_argument('-t', '--target', help='target directory', required=True)
    parser.add_argument('-v', '--verbosity', help='verbosity', required=False, type=int, default=0)
    return parser.parse_args(args)


def get_arw_files(dir_path):
    """
    :param dir_path: Directory path where ARW files live.
    :return: A list of just the ARW file names.
    """
    arw_files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    return arw_files


def get_source_files(source_dir, files):
    """
    :param source_dir: ARW directory path.
    :param files: List of ARW files in the ARW directory.
    :return: List of ARW source files.
    """
    source_files = [join(source_dir, f) for f in files]
    source_files = [f.replace('\\', '/') for f in source_files]
    return source_files


def get_target_files(target_dir, files):
    """
    :param target_dir: JPG directory path.
    :param files: List of ARW files in the ARW directory.
    :return: List of JPG target files.
    """
    target_files = [join(target_dir, f).replace('ARW', 'JPG').replace('arw', 'JPG') for f in files]
    target_files = [f.replace('\\', '/') for f in target_files]
    return target_files


def get_source_target_files(source_dir, target_dir):
    """
    :param source_dir: ARW source directory path.
    :param target_dir: JPG target directory path.
    :return: List of tuples. Each tuple has a source ARW and target JPG file path.
    """
    arw_files = get_arw_files(source_dir)
    source_files = get_source_files(source_dir, arw_files)
    target_files = get_target_files(target_dir, arw_files)
    tups = [(s, t) for s, t in zip(source_files, target_files)]
    return tups


if __name__ == "__main__":
    # python arwjpg.py -s C:/Users/super/Desktop/100MSDCF -t C:/Users/super/Desktop/out
    args = parse_args(sys.argv[1:])
    print('{} to {}'.format(args.source, args.target))
    make_dir(args.target)

    tups = get_source_target_files(args.source, args.target)
    verbosity = args.verbosity
    n_jobs = multiprocessing.cpu_count()
    results = Parallel(n_jobs=n_jobs, verbose=verbosity)(delayed(convert_raw)(tup[0], tup[1]) for tup in tqdm(tups))
    n_successes = sum(results)
    n_conversions = len(tups)
    print('{} of {} successful'.format(n_successes, n_conversions))
    
