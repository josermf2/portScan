import subprocess
import json
import xmltodict

def display_output():
    # Parse XML output to JSON
    with open("xml_file.xml") as xml_file:
        output_xml = xml_file.read()
        output_dict = xmltodict.parse(output_xml)
        output_json = json.loads(json.dumps(output_dict))

    # Extract scan statistics from JSON
    runstats = output_json.get('nmaprun', {}).get('runstats', {})
    elapsed = runstats.get('finished', {}).get('@elapsed', 'unknown')
    hosts_total = runstats.get('hosts', {}).get('@total', 'unknown')
    hosts_up = runstats.get('hosts', {}).get('@up', 'unknown')
    hosts_down = runstats.get('hosts', {}).get('@down', 'unknown')
    print(f'Scan completed in {elapsed} seconds')
    print(f'{hosts_up} out of {hosts_total} hosts scanned are up\n')

    # Extract host and port information from JSON
    hosts = output_json.get('nmaprun', {}).get('host', [])
    if isinstance(hosts, dict):
        hosts = [hosts]  # convert to list if only one host
    for host in hosts:
        if isinstance(host, dict) and host.get('status', {}).get('@state') == 'up':
            ip_address = host['address'].get('@addr', 'unknown')
            print(f'Host {ip_address} is up')
            ports = host.get('ports', {}).get('port', [])
            if isinstance(ports, dict):
                ports = [ports]
            for port in ports:
                portid = port.get('@portid', 'unknown')
                protocol = port.get('@protocol', 'unknown')
                service_name = port.get('service', {}).get('@name', 'unknown')
                print(f'  Port {portid}/{protocol} is open ({service_name})')
            print()
        elif isinstance(host, dict) and host.get('status', {}).get('@state') == 'down':
            ip_address = host['address'].get('@addr', 'unknown')
            print(f'Host {ip_address} is down or offline\n')
        else:
            print('Host scan data is missing or invalid\n')

    return


def scan_host_network(ip_address):
    # Run Nmap scan and save output to XML file
    command = "nmap " + ip_address + " -oX xml_file.xml"
    print(f'Scanning host or network at IP address: {ip_address} ...')
    subprocess.run(command, shell=True, capture_output=True, text=True)
    display_output()
    return

def scan_port_range(ip_address, port_range):
    command = "nmap -p " + port_range + " " + ip_address + " -oX xml_file.xml"
    print(f'Scanning ports {port_range} of {ip_address} ...')
    subprocess.run(command, shell=True, capture_output=True, text=True)
    display_output()
    return 

def scan_well_known_ports(ip_address):
    command = "nmap -F " + ip_address + " -oX xml_file.xml"
    print(f'Scanning ports the well known parts of {ip_address} ...')
    subprocess.run(command, shell=True, capture_output=True, text=True)
    display_output()
    return 