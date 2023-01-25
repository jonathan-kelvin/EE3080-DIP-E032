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
import pandas as pd

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

def generate_csv(path, output_dir=None, csv_name='label.csv'):
    """
    creates a csv file with 2 columns, file_name and label.
    expects data to be in format:
        data
        --real
        ----real_123.png
        --fake
        ----fake_123.png
    Args:
        path -> path to data
    """
    if output_dir is None:
        output_dir = path
    df = pd.DataFrame(columns=['file_name', 'label'])
    real_path = os.path.join(path, 'real')
    fake_path = os.path.join(path, 'fake')
    for f in tqdm(os.listdir(real_path)):
        if f.startswith('real'):
            newRow = {'file_name': f, 'label': 'real'}
            df = df.append(newRow, ignore_index=True)
    for f in tqdm(os.listdir(fake_path)):
        if f.startswith('fake'):
            newRow = {'file_name': f, 'label': 'fake'}
            df = df.append(newRow, ignore_index=True)
    df.to_csv(os.path.join(output_dir, csv_name))