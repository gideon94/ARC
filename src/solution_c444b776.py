from constants import COLORS
import numpy as np
from process_data import process


def fill_up(header, data):
    row_header = header[0]-10
    column_header = header[1]
    while(row_header >= 0):
        data[row_header][column_header] = data[header[0]][header[1]]
        row_header = row_header-10


def fill_down(header, data, limit):
    row_header = header[0]+10
    column_header = header[1]
    while(row_header <= limit):
        data[row_header][column_header] = data[header[0]][header[1]]
        row_header = row_header+10


def fill_left(header, data):
    row_header = header[0]
    column_header = header[1]-10
    while(column_header >= 0):
        data[row_header][column_header] = data[header[0]][header[1]]
        column_header = column_header-10


def fill_right(header, data, limit):
    row_header = header[0]
    column_header = header[1]+10
    while(column_header <= limit):
        data[row_header][column_header] = data[header[0]][header[1]]
        column_header = column_header+10


def copy(header, data, n_row, n_col):
    fill_left(header, data)
    fill_right(header, data, n_col)
    fill_up(header, data)
    fill_down(header, data, n_row)


def solve(data):
    n_row = data.shape[0]
    n_col = data.shape[1]
    if(n_row > 9 or n_col > 9):
        for i in range(n_row):
            for j in range(n_col):
                if(data[i][j] != COLORS['yellow'] and data[i][j] != COLORS['black']):
                    copy((i, j), data, n_row, n_col)
    return data


def main():
    process('c444b776')


if __name__ == '__main__':
    main()
