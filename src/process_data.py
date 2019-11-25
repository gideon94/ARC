import json
import numpy as np
import os
from pathlib import Path

def process(file_name):
    train_data=None
    solution = __import__('solution_' + file_name, fromlist=['solve'])
    solve=solution.solve

    with open(Path(str(Path(__file__).parents[1]) + '/data/training/' + file_name + '.json'),'r') as json_file:
        train_data=json.load(json_file)

    for data in train_data['train']:
        input_data = np.asarray(data['input'])[:]
        output_data = solve(input_data)
        print(output_data)

    for data in train_data['test']:
        input_data = np.asarray(data['input'])[:]
        output_data = solve(input_data)
        print(output_data)