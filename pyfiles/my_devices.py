#class5 module lab 2c

from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass


password = getpass()
cisco_nxos = {
        'device_type': 'cisco_nxos',
        'ip': 'nxos1.lasthop.io',
        'username': 'pyclass',
        'password': password,
#        'global_delay_factor': 2,
        'session_log': 'nxos1_output.txt'
}


net_connect = ConnectHandler (**cisco_nxos)
print(net_connect.find_prompt())

#cfg = [
#    'ip name-server 1.1.1.1',
#    'ip name-server 1.0.0.1',
#    'ip domain-lookup',
#]
#output = net_connect.send_config_set(cfg)
#print (output)

net_connect.disconnect()
