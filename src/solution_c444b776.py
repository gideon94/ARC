import numpy as np
import json
train_data = ''
with open('../data/training/c444b776.json', 'r') as json_file:
    train_data = json.load(json_file)
input_data = np.asarray(train_data['test'][0]['input'])

n_row = input_data.shape[0]
n_col = input_data.shape[1]


def traverse_up(header):
    print('traverse_up')
    row_header = header[0]-10
    column_header = header[1]
    while(row_header >= 0):
        input_data[row_header][column_header] = input_data[header[0]][header[1]]
        row_header = row_header-10


def traverse_down(header, limit):
    print('traverse_down')
    print(limit)

    row_header = header[0]+10
    print(row_header)
    column_header = header[1]
    while(row_header <= limit):
        input_data[row_header][column_header] = input_data[header[0]][header[1]]
        row_header = row_header+10


def traverse_left(header):
    print('traverse_left')
    row_header = header[0]
    column_header = header[1]-10
    while(column_header >= 0):
        input_data[row_header][column_header] = input_data[header[0]][header[1]]
        column_header = column_header-10


def traverse_right(header, limit):
    print('traverse_right')
    row_header = header[0]
    column_header = header[1]+10
    while(column_header <= limit):
        input_data[row_header][column_header] = input_data[header[0]][header[1]]
        column_header = column_header+10


def fill_data(header):
    traverse_left(header)
    traverse_right(header, n_col)
    traverse_up(header)
    traverse_down(header, n_row)


def main():
    if(n_row > 9 or n_col > 9):
        for i in range(n_row):
            for j in range(n_col):
                if(input_data[i][j] != 4 and input_data[i][j] != 0):
                    fill_data((i, j))

    print(input_data)


main()
