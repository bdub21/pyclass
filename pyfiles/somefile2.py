#CDP neighbor details for devices.

from __future__ import print_function, unicode_literals

from netmiko import Netmiko
from datetime import datetime
from getpass import getpass

net_connect.enable()
print(net_connect.find_prompt())

output = net_connect.send_command('sh cdp ne detail', delay_factor=2)
print (output)
