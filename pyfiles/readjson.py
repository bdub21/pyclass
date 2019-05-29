import json
from pprint import pprint

# filename = 'example.json'
filename = input('Enter filename: ')
with open(filename) as f:
    data = json.load(f)
pprint(data)
