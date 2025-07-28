import socket

def scan_network(ip_range, ports):
    open_ports = []
    port_list = list(map(int, ports.split('-')))
    for port in range(port_list[0], port_list[1] + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((ip_range, port)) == 0:
                open_ports.append((ip_range, port))
            s.close()
        except:
            continue
    return open_ports
