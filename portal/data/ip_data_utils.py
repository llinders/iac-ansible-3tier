import json

__AVAILABLE_IP_ADDRESSES_FILE__ = './portal/data/available_ip_addresses.json'

def find_next_available_ips(amount) -> list:
    ip_data: dict
    with open(__AVAILABLE_IP_ADDRESSES_FILE__, 'r') as f:
        ip_data = json.load(f)

    return ip_data[0:amount]

