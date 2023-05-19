import json

__AVAILABLE_IP_ADDRESSES_FILE__ = r'./portal/data/available_ip_addresses.json'

def find_next_available_ips(amount: int) -> list[str]:
    ip_data: list
    with open(__AVAILABLE_IP_ADDRESSES_FILE__, 'r') as f:
        ip_data = json.load(f)

    return ip_data[0:amount]

def remove_ips(ip_list: list[str]) -> None:
    ip_data: list
    with open(__AVAILABLE_IP_ADDRESSES_FILE__, 'r') as f:
        ip_data = json.load(f)
        
    for ip in ip_list:
            ip_data.remove(ip)

    with open(__AVAILABLE_IP_ADDRESSES_FILE__, 'w') as f:
        json.dump(ip_data, f)

def add_ips(ip_list: list[str]) -> None:
    ip_data: list
    with open(__AVAILABLE_IP_ADDRESSES_FILE__, 'r') as f:
        ip_data = json.load(f)

    ip_data += ip_list
    ip_data.sort()
    ip_data.sort(key=len) # sort first alphabetically and then by length to get the required result
    
    with open(__AVAILABLE_IP_ADDRESSES_FILE__, 'w') as f:
        json.dump(ip_data, f)

