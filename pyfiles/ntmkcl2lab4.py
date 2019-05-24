#!/usr/bin/env python
#Issue list of commands

from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

cisco_ios = {
        'device_type': 'cisco_ios',
        'ip': 'cisco3.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'global_delay_factor': 2,
}

net_connect = ConnectHandler (**cisco_ios)
print(net_connect.find_prompt())

cfg = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup',
]
output = net_connect.send_config_set(cfg)
print (output)

net_connect.disconnect()
