import numpy as np
from process_print import process
import json


def solve(input_data):
    # Finds all unique elements and thier count
    unique, count = np.unique(input_data, return_counts=True)

    # Convert to dictionary and sort
    map_dict = dict(zip(unique, count))
    del map_dict[0]
    sort_dict = {k: map_dict[k] for k in sorted(
        map_dict, key=map_dict.get, reverse=True)}

    # Print the result list
    result = list()
    for i in sort_dict.keys():
        result.append(i)
    result = np.asarray(result)[np.newaxis].T
    return result


def main():
    process('f8ff0b80')


if __name__ == '__main__':
    main()
