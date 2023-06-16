import json


__CUSTOMER_INVENTORY_FILE = 'portal/data/customer_data.json'

def get_customer(customer_number: int) -> dict:
    '''Get data from a specific customer'''
    customers = _load_all_customer_data()
    for customer in customers:
        if (customer['customer_number'] == customer_number):
            return customer
        raise Exception(f'Customer with customer number {customer_number} could not be found')
    return {}

def write_new_customer(username: str) -> int:
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

    with open(__CUSTOMER_INVENTORY_FILE, 'w') as inv_file:
        json.dump(customer_data, inv_file, indent=4)

    return new_customer_number

def update_customer(customer_number: int, customer_data: dict) -> None:
    """
    Update customer taking in a customer dict and replacing the old customer data
    """
    customers = _load_all_customer_data()
    for index, customer in enumerate(customers):
        if (customer['customer_number'] == customer_number):
            customers[index] = customer_data
    
    with open(__CUSTOMER_INVENTORY_FILE, 'w') as f:
        json.dump(customers, f, indent=4)


def check_if_exists(customer_number: int):
    """
    Checks if a customer exists with `customer_number` and returns True if it does
    """
    customers = _load_all_customer_data()
    for customer in customers:
        if customer.get('customer_number') == customer_number: return True
    return False

def environment_deployed(customer_number: int, env: str) -> bool:
    if env == 'test':
        customers = _load_all_customer_data()
        for customer in customers:
            if customer.get('customer_number') == customer_number:
                return customer['test_env_setup']['deployed']
    elif env == 'prod':
        customers = _load_all_customer_data()
        for customer in customers:
            if customer.get('customer_number') == customer_number:
                return customer['prod_env_setup']['deployed']
    raise ValueError('Not a valid environment, please enter `test` or `prod`')
    return False


def _load_all_customer_data() -> list:
    ''' Load all customer data from customer inventory file '''
    with open(__CUSTOMER_INVENTORY_FILE, 'r') as f:
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