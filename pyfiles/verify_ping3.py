#!/usr/bin/env python
#Send ping command using timing

from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

cisco3 = {
        'device_type': 'cisco_ios',
        'ip': 'cisco3.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'port': 22
}

net_connect = ConnectHandler (**cisco3)

output = net_connect.send_command_timing(
    "ping", strip_prompt=False, strip_command=False
)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing(
    "8.8.8.8", strip_prompt=False, strip_command=False
)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)

print()
print (output)
print()

net_connect.disconnect()
