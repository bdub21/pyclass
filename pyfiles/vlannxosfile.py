#!/usr/bin/env python
#VLANS for NXOS1 & NXOS2

import netmiko
from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

cisco_nxos1 = {
        'device_type': 'cisco_nxos',
        'ip': 'nxos1.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'port': 22,
        'global_delay_factor': 2,
}
cisco_nxos2 = {
        'device_type': 'cisco_nxos',
        'ip': 'nxos2.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'port': 22,
        'global_delay_factor': 2,
}

all_devices = [cisco_nxos1,cisco_nxos2]


for devices in all_devices:
    net_connect = ConnectHandler (**devices)
    output = net_connect.send_config_from_file('my_commands.txt')
    print (output)


print(net_connect.find_prompt())

net_connect.disconnect()
