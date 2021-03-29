from os import listdir
from os.path import isfile, join
# * Return a list of filenames in directory path


def read_files_from_dir(path):
    return [f for f in listdir(path) if isfile(join(path, f))]
