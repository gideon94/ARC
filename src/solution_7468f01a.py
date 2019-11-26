import numpy as np
from process_print import process
import json


def solve(input_data):
    print(input_data)
    mask = (input_data != 0)
    x = np.any(mask, axis=1).sum()
    result = input_data[mask].reshape(x, -1)
    return result


def main():
    process('7468f01a')


if __name__ == '__main__':
    main()
