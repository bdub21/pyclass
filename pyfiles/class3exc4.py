import json
from pprint import pprint

filename = "class3exc4.json"
with open(filename) as f:
    arp_data = json.load(f)

arp_dict = {}
arp_entries = arp_data["ipV4Neighbors"]
for entry in arp_entries:
    ip_addr = entry["address"]
    mac_addr = entry["hwAddress"]
    arp_dict[ip_addr] = mac_addr

print()
pprint(arp_dict)
print()
