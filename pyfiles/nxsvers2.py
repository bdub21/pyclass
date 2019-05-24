#!/usr/bin/env python
#Get running-config from nxos in lab with for loop

from __future__ import print_function, unicode_literals

from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

cisco_nxos1 = {
        'device_type': 'cisco_nxos',
        'ip': 'nxos1.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'port': 22,
        'session_log':'nxos1.txt'
}

cisco_nxos2 = {
        'device_type': 'cisco_nxos',
        'ip': 'nxos2.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'port': 22,
        'session_log': 'nxos2.txt'
}

all_devices = [cisco_nxos1,cisco_nxos2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    print(net_connect.find_prompt())
    output = net_connect.send_command('show version')
    print (output)


#net_connect = ConnectHandler (**cisco_nxos1)
#Ensure enable mode
#net_connect.enable()
#print(net_connect.find_prompt())
#output = net_connect.send_command('show version')
#print (output)

net_connect.disconnect()
