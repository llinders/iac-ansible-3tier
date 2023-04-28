import json

__CUSTOMER_INVENTORY_FILE__ = 'portal/data/customer_data.json'

def get_customer(customer_number: int) -> dict:
    '''Get data from a specific customer'''
    customers = _load_all_customer_data()
    for customer in customers:
        if (customer['customer_number'] == customer_number):
            return customer
        print('Customer with customer number %d could not be found'%customer_number)

def write_new_customer(username: str):
    '''Register a new customer'''
    new_customer_number = _find_available_customer_number()
    
    new_customer_profile = {
        'customer_number': new_customer_number,
        'username': username,
        'test_env_setup': {
            'deployed': 'false'
        },
        'prod_env_setup': {
            'deployed': 'false'
        }
    }

    customer_data = _load_all_customer_data()
    customer_data.append(new_customer_profile)

    with open(__CUSTOMER_INVENTORY_FILE__, 'w') as inv_file:
        json.dump(customer_data, inv_file, indent=4)

def update_customer(customer_number: int):
    return

def check_if_exists(customer_number: int):
    '''Checks if a customer exists with `customer_number` and returns True if it does'''
    customers = _load_all_customer_data()
    for customer in customers:
        if customer.get('customer_number') == customer_number: return True
    return False

def environment_deployed(env: str, customer_number: int):
    if env == 'test':
        customers = _load_all_customer_data()
        for customer in customers:
            if customer.get('customer_number') == customer_number:
                return customer['test_env_setup']['deployed']
    elif env == 'prod':
        customers = _load_all_customer_data()
    else:
        print('Not a valid environment, please enter `test` or `prod`')


def _load_all_customer_data() -> dict:
    ''' Load all customer data from customer inventory file '''
    with open(__CUSTOMER_INVENTORY_FILE__, 'r') as f:
        customer_data = json.load(f)
    return customer_data

def _find_available_customer_number():
    ''' Private function
    Find next available customer number 
    '''
    customer_data = _load_all_customer_data()
        
    customer_numbers = []
    for customer in customer_data:
        customer_numbers.append(customer['customer_number'])
    
    return int(max(customer_numbers))+1