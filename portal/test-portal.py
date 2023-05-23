# from menu.menu_navigation import Menu, show_menu
# import utils.data.customer_data_utils as cdu
# import utils.data.ip_data_utils as idu
# from utils.deployment.j2_template_modifier import modify_vagrantfile_testenv
from utils.customer_context_manager import CustomerContextManager

## Loading all customer data ##
#print(cdu._load_all_customer_data())

## Adding a customer to the file ##
# portal.add_customer_to_file('test')
# print(portal.load_customer_data())

## Test printing menus ##
# show_menu(Menu.STARTUP_MENU)
# show_menu(Menu.NEW_CUSTOMER)

# Filter customer
# customers = cdu._load_all_customer_data()
# for customer in customers:
#     if customer['customer_number'] == 3:
#         print('Found customer ' + '3')
#         print(customer)
    
# Show existing customer menu
#show_menu(Menu.LOGIN)

# Test environment_deployed function
# print(cdu.environment_deployed('test', 1))
# print(cdu.environment_deployed('test', 2))

## Test ip_data_utils ##
# find_next_available_ip()
#print(idu.find_next_available_ips(3))


## j2_template_modifier ##
# test env
# print(modify_vagrantfile_testenv('0.0.0.0', '1.1.1.1'))

## Test ip_data_utils.py
# idu.add_ips(['0.0.0.0', '0.0.0.1'])

## Test file copying and j2 template modify
# ccm = CustomerContextManager(1)
#ccm.deploy_new_test_environment()

## Test object to dict transformation
ccm = CustomerContextManager(1)
print(dict(ccm.__customer))

## Test update customer method
ccm.__customer.username = ccm.__customer.username + '1'
ccm.__persist_customer_data()