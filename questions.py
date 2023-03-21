actions = [
    {
        'type': 'list',
        'name': 'action',
        'message': 'What do you want to do?',
        'choices': [
            'Scan an host or a network',
            'Scan a port range on a host',
            'Scan the well known ports on a host',
            'Quit Port Scan Tool'
        ]
    }
]

host_network_ip = [
    {
        'type': 'input',
        'name': 'host_network_ip',
        'message': 'What is the IP address or the network you want to scan?'
    }
]

port_range = [
    {
        'type': 'input',
        'name': 'port_range',
        'message': 'What is the port range you want to scan?'
    }
]

