import numpy as np
from process_data import process
import json

def solve(input_data):
    mask = (input_data != 0) # mask the index of the pattern in input_data 
    x = np.any(mask, axis=1).sum() # get the indexes of the pattern
    result = input_data[mask].reshape(x, -1) # reshape the input_data to extract pattern
    return np.fliplr(result) # mirrors the pattern and returns result

def main():
    process('7468f01a')

if __name__ == '__main__':
    main()
