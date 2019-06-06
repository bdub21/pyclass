from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
import json
from pprint import pprint


#env = Environment()
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')


nxos_vars = {
    "nxos_host1": 'nxos1',
    "intf1_nxos": 'Ethernet1/1',
    "network1": '10.1.100.1/24',
    "local_as": 10,
    "remote_as": 22,
    "nxos_host2": 'nxos2',
    "intf2_nxos": 'Ethernet1/1',
    "network2": '10.1.100.2/24',
}

nxos1 = [nxos_vars]
nxos2 = [nxos_vars]

for config in nxos1:
    nxos_template = 'nxos_config1.j2'
    exc3_template = env.get_template(nxos_template)
#exc_template = Template(nxos_template)
    output1 = exc3_template.render(**nxos_vars)
    f = open("bgp_nxos1output.txt", "a")
    print(output1, file = f)
    f.close()
#    print(output1)

for config in nxos2:
    nxos_template = 'nxos_config2.j2'
    exc3_template = env.get_template(nxos_template)
    output2 = exc3_template.render(**nxos_vars)
    ff = open("bgp_nxos2output.txt", "a")
    print(output2, file = ff)
    ff.close()
#    print(output2)


import my_devices2
