"""topN: returns top numbers from file"""

from os import path
from sys import argv
import numpy as np
import pandas as pd


def get_args():
    """Process command arguments for topN.

    Args:
        None

    Returns:
        file_path (str): Path of file for parsing.
        max_nums (int): Number of maximum numbers to track.

    Raises:
        ValueError: If arguments are not a file and a number.
    """

    file_path = ''
    max_nums = ''

    if argv[1].isalnum() and path.isfile(argv[2]):
        file_path = argv[2]
        max_nums = int(argv[1])
    elif path.isfile(argv[1]) and argv[2].isalnum():
        file_path = argv[1]
        max_nums = int(argv[2])
    else:
        raise ValueError("topN: invalid command arguments: "
                         "'{}' and '{}'".format(argv[1], argv[2]))

    return file_path, max_nums


def main():
    """Parses an arbitrarily large file of individual numbers each line,
    and prints a set of the largest numbers"""

    file_path, max_nums = get_args()

    top_nums = np.zeros(max_nums)
    data = pd.read_table(
        filepath_or_buffer=file_path,
        header=None,
        chunksize=1024,
    )

    for chunk in data:
        chunk = chunk.as_matrix()
        for num in chunk:
            min_num = top_nums.min()
            if num > min_num:
                top_nums[top_nums.argmin()] = num

    top_nums[:: -1].sort()
    print(top_nums)


if __name__ == '__main__':
    main()
