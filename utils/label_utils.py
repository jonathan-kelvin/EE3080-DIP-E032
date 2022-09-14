import os
import glob
from posixpath import splitext
import shutil
import ntpath
from tqdm import tqdm
from shutil import copyfile
import argparse
import zipfile
import shutil
import os.path

def rename(input_dir, prefix=None, output_dir=None):
    """
    renames all files in a folder recursively with format prefix_<num>.
    Args:
        input_dir -> path to desired folder
        prefix -> desired prefix, default is name of folder
        output_dir -> path to output folder, default is input_dir
    """

    if output_dir is None:
        output_dir = input_dir
    if prefix is None:
        prefix = ntpath.split(input_dir)[-1]
    count = 0
    for img in tqdm(glob.glob(input_dir + "/**/*.*", recursive=True)):
        _, file_name = ntpath.split(img)
        file_id, file_ext = os.path.splitext(file_name)
        count += 1
        new_file_name = "{}_{}{}".format(prefix, count, file_ext)
        new_file_path = os.path.join(output_dir, new_file_name)
        shutil.copy(img, new_file_path)