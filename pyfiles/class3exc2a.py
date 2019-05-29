import yaml
from pprint import pprint

cisco1 = {"device_name": "cisco1", "host": "cisco1.lasthop.io"}

cisco2 = {"device_name": "cisco2", "host": "cisco2.lasthop.io"}

cisco3 = {"device_name": "cisco3", "host": "cisco3.lasthop.io"}

cisco4 = {"device_name": "cisco4", "host": "cisco4.lasthop.io"}

mydevices = [cisco1, cisco2, cisco3, cisco4]
for device in mydevices:
    device["username"] = "admin"
    device["password"] = "cisco123"

print()
pprint(mydevices)
print()

with open("mydevices.yml", "w") as f:
    yaml.dump(mydevices, f, default_flow_style=False)
