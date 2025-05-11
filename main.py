
from shadowmap.scanner import scan_network
from shadowmap.detector import detect_hidden_services
from shadowmap.report_generator import generate_report

if __name__ == "__main__":
    target_network = input("Enter the network to scan (e.g., 192.168.1.0/24): ")
    scan_data = scan_network(target_network)
    results = detect_hidden_services(scan_data)
    generate_report(results)
