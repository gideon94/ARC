import numpy as np
from process_data import process
from constants import COLORS

def solve(data):
    # postions having non-zero elements
    position_non_zeros = np.nonzero(data)
    
    # find min and max of row and column indices to find the rectangle or sqaure shape
    min_row_position = min(position_non_zeros[0])
    max_row_position = max(position_non_zeros[0])
    min_col_position = min(position_non_zeros[1])
    max_col_position = max(position_non_zeros[1])

    # tranverse through the rectangle/square and fill blacks with red
    for i in range(min_row_position, max_row_position + 1):
        for j in range(min_col_position, max_col_position + 1):
            if data[i, j] == COLORS["black"]:
                data[i, j] = COLORS["red"]

    return data

def main():
    process("6d75e8bb")

if __name__ == "__main__":
    main()