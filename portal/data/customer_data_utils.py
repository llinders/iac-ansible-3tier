import json

CUSTOMER_INVENTORY_FILE = 'portal/data/customer_data.json'

def load_customer_data():
    ''' Load customer data from customer inventory file '''
    with open(CUSTOMER_INVENTORY_FILE, 'r') as f:
        customer_data = json.load(f)
    return customer_data

def write_new_customer(username):
    new_customer_number = find_available_customer_number()
    
    new_customer_profile = {
        'customer_number': new_customer_number,
        'username': username,
        'test_env_setup': {
            'deployed': 'false'
        },
        'prod_env_setup': {
            'deployed': 'false',
            'number_of_webservers': '0'
        }
    }

    customer_data = load_customer_data()
    customer_data.append(new_customer_profile)

    with open(CUSTOMER_INVENTORY_FILE, 'w') as inv_file:
        json.dump(customer_data, inv_file, indent=4)