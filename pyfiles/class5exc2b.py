from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

#env = Environment()
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

#filename = 'nxos_config1.j2'
#with open(filename) as f:
#    nxos_template = f.read()


nxos_vars = {
    "nxos_host1": 'nxos1',
    "intf_nxos": 'Ethernet1/1',
    "nxos_host2": 'nxos2',
    "network1": '10.1.100.1/24',
    "network2": '10.1.100.2/24',
    "local_as": 10,
    "remote_as": 22,
    }


nxos_template = 'nxos_config2.j2'
exc3_template = env.get_template(nxos_template)
#exc_template = Template(nxos_template)
output = exc3_template.render(**nxos_vars)
print(output)
