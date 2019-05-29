import json

my_data = {
    'device_name': 'cisco1',
    'host': 'cisco1.lasthop.io',
    'username': 'admin',
    'password': 'cisco',
}

some_list = list(range(10))
my_data['some_list'] = some_list
my_data['null_value'] = None
my_data['a bool'] = False

filename = 'output.json'
with open(filename, 'wt') as f:
    #json.dump(my_data, f)
    json.dump(my_data, f, indent=4)

# Print out.

print("Python")
print("#" * 10)
print(my_data)
print()
print("JSON")
print("#" * 10)
print(json.dumps(my_data))
