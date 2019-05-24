#!/usr/bin/env python
#Get show_version & show_lldp from cisco4 in lab


from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

cisco_ios = {
        'device_type': 'cisco_ios',
        'ip': 'cisco4.lasthop.io',
        'username': 'pyclass',
        'password': getpass()
}

net_connect = ConnectHandler (**cisco_ios)
print (net_connect.find_prompt())



output = net_connect.send_command('show version', use_textfsm=True)
print (output)
output = net_connect.send_command('show lldp neighbors', use_textfsm=True)
print (output)

net_connect.disconnect()
