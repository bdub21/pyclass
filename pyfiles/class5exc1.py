from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined, Template
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

bgp_config1 = '''
router bgp {{ local_as }}
  neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{ peer2_ip }} remote-as {{ peer2_as }}
    address-family ipv4 unicast
'''

#bgp_template = bgp_config1
#exc1_template = Template(bgp_template)
#output = exc1_template.render(local_as=10, peer1_ip='10.1.20.2', peer1_as=20, peer2_ip='10.1.30.2', peer2_as=30)

bgp_vars = {
    "local_as": 10,
    "peer1_ip": '10.1.20.2',
    "peer1_as": 20,
    "peer2_ip": '10.1.30.2',
    "peer2_as": 30, 
    }

bgp_template = bgp_config1
exc1_template = Template(bgp_template)
output = exc1_template.render(**bgp_vars)

print(output)
print()
