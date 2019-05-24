#!/usr/bin/env python
#Get running-config from nxos in lab

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
        #'session_log': 'my_session.txt'
}

net_connect = ConnectHandler (**cisco_nxos1)

#Ensure enable mode
net_connect.enable()
print(net_connect.find_prompt())

#output = net_connect.send_command('show version')

#print (output)

#net_connect.disconnect()
