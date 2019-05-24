#!/usr/bin/env python
#simple show cmds

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device = {
    "device_type": "cisco_ios",
    "host": "cisco2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
#    "global_delay_factor": 2,
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip arp", use_textfsm=True)
print(output)

net_connect.disconnect()
