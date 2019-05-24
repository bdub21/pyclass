#!/usr/bin/env python
#Netmiko task6 d thru g

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
net_connect.enable()
print(net_connect.find_prompt())
#write channel 'disable'
net_connect.write_channel('disable\n')
print(net_connect.find_prompt())
#read channel
output = net_connect.read_channel()
print(output)
net_connect.secret = getpass()
net_connect.enable()
print(net_connect.enable())
net_connect.find_prompt()
print(net_connect.find_prompt())
net_connect.disconnect()
