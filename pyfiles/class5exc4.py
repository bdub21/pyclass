from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined, Template
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

vrf_vars = {
    'protocol': 'ipv4',
    'rd': '100',
    'vrf_name': 'blue',
}


#intf_vars = {'primary_ip': True}
#intf_vars = {'primary_ip': False}

vrf_template = 'vrf_ipv4-6_loop.j2'
exc3_template = env.get_template(vrf_template)
#exc2_template = Template(intf_template)
output = exc3_template.render(**vrf_vars)

f = open("vrfloop_output.txt", "a")
print(output, file = f)
f.close()
print(output)
