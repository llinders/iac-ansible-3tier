from menu.menu_navigation import Menu, show_menu
import data.customer_data_utils as cdu

## Loading all customer data ##
print(cdu._load_all_customer_data())

## Adding a customer to the file ##
# portal.add_customer_to_file('test')
# print(portal.load_customer_data())

## Test printing menus ##
# show_menu(Menu.STARTUP_MENU)
# show_menu(Menu.NEW_CUSTOMER)

# Filter customer
customers = cdu._load_all_customer_data()
for customer in customers:
    if customer['customer_number'] == 3:
        print('Found customer ' + '3')
        print(customer)
    
# Show existing customer menu
show_menu(Menu.LOGIN)