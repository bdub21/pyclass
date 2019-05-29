import yaml
from os import path
from netmiko import ConnectHandler


home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    yaml_out = yaml.load(f)

cisco_ios = yaml_out["cisco3"]
net_connect = ConnectHandler(**cisco_ios)

print()
print(net_connect.find_prompt())
print()

net_connect.disconnect()
