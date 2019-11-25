import numpy as np
from scipy.sparse import csr_matrix
from process_data import process
from constants import COLORS

def solve(data):
    n_row = data.shape[0]
    n_column = data.shape[1]
    non_zero_rows=[]
    non_zero_transposed=[]
    for i in range(n_row):
        if( np.any(data[i] != COLORS['black']) == True):
            non_zero_rows.append(data[i])
    non_zero_rows=np.asarray(non_zero_rows)
    for i in range(n_column):
        if( np.any(non_zero_rows[:, i] != COLORS['black']) == True):
            non_zero_transposed.append(non_zero_rows[:, i])
    non_zero_matrix= np.asarray(non_zero_transposed).T
    non_zero_matrix=np.where(non_zero_matrix==COLORS['black'], COLORS['red'], non_zero_matrix)
    return non_zero_matrix

def main():
    process('6d75e8bb')

if __name__ == '__main__':
    main()