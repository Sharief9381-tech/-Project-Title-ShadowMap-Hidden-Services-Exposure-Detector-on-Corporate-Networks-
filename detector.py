import shodan
from .config import SHODAN_API_KEY

def detect_hidden_services(scan_data):
    detected = []

    if not SHODAN_API_KEY:
        print("[!] Shodan API key not set. Skipping passive detection.")
        return scan_data  # Skip if API key is not provided

    api = shodan.Shodan(SHODAN_API_KEY)

    for host_data in scan_data:
        ip = host_data['ip']
        try:
            shodan_data = api.host(ip)
            exposed_ports = [item['port'] for item in shodan_data['data']]
            current_ports = [p['port'] for p in host_data['ports']]
            hidden_ports = list(set(current_ports) - set(exposed_ports))

            if hidden_ports:
                host_data['hidden_ports'] = hidden_ports
                detected.append(host_data)
        except Exception as e:
            print(f"[-] Could not query Shodan for {ip}: {e}")

    return detected
