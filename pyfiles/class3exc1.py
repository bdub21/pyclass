#!/usr/bin/env python
#Get show_version & show_lldp from cisco4 in lab


from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

cisco_ios = {
        'device_type': 'cisco_ios',
        'ip': 'cisco1.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'session_log': 'my_arpoutput.txt',
}

net_connect = ConnectHandler (**cisco_ios)
print (net_connect.find_prompt())

output = net_connect.send_command('show ip arp', use_textfsm=True)

new_intf = output[0]

#['mac']['address']['interface']

for intf in new_intf.items():
    print(intf['mac'])
    print()

#output = net_connect.send_command('show lldp neighbors', use_textfsm=True)
#print (output)

net_connect.disconnect()
