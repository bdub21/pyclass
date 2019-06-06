from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
import json
import sys
from pprint import pprint

#env = Environment()
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

nxos1_vars = {
    "nxos_host1": 'nxos1',
    "intf_nxos": 'Ethernet1/1',
    "network1": '10.1.100.1/24',
}

nxos2_vars = {
    "nxos_host2": 'nxos2',
    "intf_nxos": 'Ethernet1/1',
    "network2": '10.1.100.2/24',
}

bgp_vars = {
    "local_as": 10,
    "remote_as": 22,
}

nxos1 = [nxos1_vars]
nxos2 = [nxos2_vars]
bgp = [bgp_vars]

for template1 in nxos1:
    nxos_template = 'nxos_config2.j2'
    exc3_template = env.get_template(nxos_template)
    output1 = exc3_template.render(template1)

for template2 in nxos2:
    nxos_template = 'nxos_config2.j2'
    exc3_template = env.get_template(nxos_template)
    output2 = exc3_template.render(template2)

for template3 in bgp:
    nxos_template = 'nxos_config2.j2'
    exc3_template = env.get_template(nxos_template)
    output3 = exc3_template.render(template3)

print(output1)
print(output2)
print(output3)
