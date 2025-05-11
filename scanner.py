

import nmap

def scan_network(network_range):
    scanner = nmap.PortScanner()
    print(f"[+] Scanning network: {network_range}")
    scanner.scan(hosts=network_range, arguments='-sS -T4')
    results = []

    for host in scanner.all_hosts():
        if scanner[host].state() == 'up':
            open_ports = []
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                for port in ports:
                    service = scanner[host][proto][port]['name']
                    open_ports.append({'port': port, 'service': service})
            results.append({'ip': host, 'ports': open_ports})

    return results
