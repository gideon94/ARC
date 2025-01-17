import json
import numpy as np
from pathlib import Path

def process(file_name):
    file_data=None
    
    # Dynamic import of solve from the file name given
    solution = __import__('solution_' + file_name, fromlist=['solve'])
    solve=solution.solve

    # Load the json file
    with open(Path(str(Path(__file__).parents[1]) + '/data/training/' + file_name + '.json'),'r') as json_file:
        file_data=json.load(json_file)

    # For every train data call solve
    for data in file_data['train']:
        input_data = np.asarray(data['input'])[:]
        output_data = solve(input_data)
        print(output_data)

    # For every test data call solve
    for data in file_data['test']:
        input_data = np.asarray(data['input'])[:]
        output_data = solve(input_data)
        print(output_data)