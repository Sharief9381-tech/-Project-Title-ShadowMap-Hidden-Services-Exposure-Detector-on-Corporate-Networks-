import json
from .config import OUTPUT_FILE

def generate_report(data):
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"[+] Report generated: {OUTPUT_FILE}")
