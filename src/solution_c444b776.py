from constants import COLORS
import numpy as np
from process_data import process

def solve(data):
    # number of rows in the 2d numpy array
    n_row = data.shape[0]

    # number of rows in the 2d numpy array
    n_col = data.shape[1]

    # postions where the colors are other than black and yellow
    positions_filled = np.where((data != COLORS["yellow"]) & (data != COLORS["black"]))

    # will contain key value pair of ((position in 9*9 array), value)
    position_values = {}

    # actual position of non-zero elements
    positions_actual = zip(positions_filled[0], positions_filled[1])

    # make a dictionary of {(position in 9*9 array), value} in a 9*9 matrix
    for position in positions_actual:
        position_values[(position[0] % 10, position[1] % 10)] = data[position]
        
    # copy the value of the position from the dictionary to every 9*9 matrix
    for i in range(n_row):
        for j in range(n_col):
            if ((i % 10, j % 10)) in position_values.keys():
                data[(i, j)] = position_values[(i % 10, j % 10)]

    return data

def main():
    process("c444b776")

if __name__ == "__main__":
    main()
