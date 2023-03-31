import portal
from menu.menu import Menu, show_menu

# Loading all customer data
print(portal.load_customer_data())

# Adding a customer to the file
portal.add_customer_to_file('test')
print(portal.load_customer_data())

# Test printing menus
show_menu(Menu.STARTUP_MENU)
show_menu(Menu.NEW_CUSTOMER)