from shadowmap.scanner import scan_network
from shadowmap.detector import detect_hidden_services
from shadowmap.report_generator import generate_report

if __name__ == "__main__":
    print("🔍 ShadowMap started.")  # Add this line to verify script runs
    target_network = input("Enter the network to scan (e.g., 127.0.0.1 or 192.168.1.0/24): ")
    scan_data = scan_network(target_network)
    results = detect_hidden_services(scan_data)
    generate_report(results)
