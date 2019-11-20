import numpy as np
import json
train_data = ''
with open('../data/training/f8ff0b80.json', 'r') as json_file:
    train_data = json.load(json_file)
input_data = np.asarray(train_data['train'][0]['input'])
print(input_data)

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
print(result)
