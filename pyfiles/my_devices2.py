#class5 module lab 2c

from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

password = getpass()
cisco_nxos1 = {
        'device_type': 'cisco_nxos',
        'ip': 'nxos1.lasthop.io',
        'username': 'pyclass',
        'password': password,
#        'global_delay_factor': 2,
        'session_log': 'nxos1_output.txt'
}

cisco_nxos2 = {
        'device_type': 'cisco_nxos',
        'ip': 'nxos2.lasthop.io',
        'username': 'pyclass',
        'password': password,
#        'global_delay_factor': 2,
        'session_log': 'nxos2_output.txt'
}

nxos1 = [cisco_nxos1]
nxos2 = [cisco_nxos2]

for devices in nxos1:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_from_file('bgp_nxos1output.txt')
#    print (net_connect.find_prompt())
for devices in nxos2:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_from_file('bgp_nxos2output.txt')
#    print (net_connect.find_prompt())

#with open('nxos2.txt') as f:
#    lines = f.read().splitlines()
#print (lines)

#net_connect = ConnectHandler (cisco_nxos1,cisco_nxos2)
#print(net_connect.find_prompt())

#cfg = [
#    'ip name-server 1.1.1.1',
#    'ip name-server 1.0.0.1',
#    'ip domain-lookup',
#]
#output = net_connect.send_config_set(cfg)
#print (output)

net_connect.disconnect()
