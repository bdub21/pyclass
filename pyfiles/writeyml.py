import yaml

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

filename = 'output.yml'
with open(filename, 'wt') as f:
    yaml.dump(my_data, f, default_flow_style=True)
