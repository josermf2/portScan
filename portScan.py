from PyInquirer import prompt
import time
from questions import *
from functions import *

print('-------------------------------------------')
print('       Welcome to the Port Scan Tool       ')
print('-------------------------------------------')
time.sleep(2)

running = True

while running:
    first_question = prompt(actions)
    if (first_question['action'] == 'Scan an host or a network'):
        host_network = prompt(host_network_ip)
        scan = scan_host_network(host_network['host_network_ip'])
    elif (first_question['action'] == 'Scan a port range on a host'):
        host_network = prompt(host_network_ip)
        port_range = prompt(port_range)
        scan = scan_port_range(host_network['host_network_ip'], port_range['port_range'])
    elif (first_question['action'] == 'Scan the well known ports on a host'):
        host_network = prompt(host_network_ip)
        scan = scan_well_known_ports(host_network['host_network_ip'])
    elif (first_question['action'] == 'Quit Port Scan Tool'):
        running = False
        print('Thank you for using the Port Scan Tool')
        time.sleep(1)
        print('Goodbye!')

