#!/usr/bin/env python
#Netmiko task6 a thru g

from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

password = getpass()
cisco_ios = {
        'host': 'cisco4.lasthop.io',
        'username': 'pyclass',
        'password': password,
        'secret': password,
        'device_type': 'cisco_ios',
        'session_log': 'my_output.txt',
}
net_connect = ConnectHandler (**cisco_ios)
#print prompt
print(net_connect.find_prompt())
#config mode
net_connect.config_mode()
print(net_connect.find_prompt())
#exit config mode
net_connect.exit_config_mode()
print(net_connect.find_prompt())

net_connect.disconnect()
