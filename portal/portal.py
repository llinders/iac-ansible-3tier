import vagrant
import os
import sys
from fabric.api import *
import json
from art import tprint

CUSTOMER_INVENTORY_FILE = 'portal/customer_inv.json'

def menu():
    ''' Main menu '''
    
    chosen_element = 0;
    
    print("#############################################################################")
    print("########                                                             ########")
    print("########                 Mijn Self Service Portal                    ########")
    print("######## ----------------------------------------------------------- ########")
    print("########             Doe iets met Vagrant en Ansible files           ########")
    print("######## ----------------------------------------------------------- ########")
    print("########                                                             ########")
    print("########                    Kies een optie :                         ########")
    print("########                                                             ########")
    print("########             1) Klant1 VM  |  2) Klant 2 VM                  ########")
    print("########             3) Klant3 VM  |  4) Klant 4 VM                  ########")
    print("########      5) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Geef een nummer van 1 tot 5: ")
    
    if int(chosen_element) == 1:
        print('Deploy Klant 1VM')
        os.chdir('klant1')
        v = vagrant.Vagrant()
        v.up() 
    elif int(chosen_element) == 2:
        print('Deploy Klant 2VM')
        os.chdir('klant2')
        v = vagrant.Vagrant()
        v.up() 
    elif int(chosen_element) == 3:
        print('Deploy Klant 3VM')
        os.chdir('klant3')
        v = vagrant.Vagrant()
        v.up() 
    elif int(chosen_element) == 4:
        print('Deploy Klant 4VM')
        os.chdir('klant4')
        v = vagrant.Vagrant()
        v.up() 
    elif int(chosen_element) == 5:
        sys.exit()
    else:
        print('Sorry, de waarde moet tussen 1 en 5 zijn')

def main_menu():
    ''' Main menu '''

    chosen_element = 0

    print("#############################################################################")
    print("########                                                             ########")
    print("########                   Self Service Portal                       ########")
    print("######## ----------------------------------------------------------- ########")
    print("########        Are you a new customer or existing customer?         ########")
    print("######## ----------------------------------------------------------- ########")
    print("########                                                             ########")
    print("########                         Choose:                             ########")
    print("########                                                             ########")
    print("########           1) New customer  |  2) Existing customer          ########")
    print("########      3) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Choose a number between 1 and 3: ")

    if int(chosen_element) == 1:
        new_customer()
    elif int(chosen_element) == 2:
        existing
    else:
        print('You have to enter a value between 1 and 3')

def load_customer_data():
    ''' Load customer data from customer inventory file '''
    with open(CUSTOMER_INVENTORY_FILE, 'r') as f:
        customer_data = json.load(f)['customers']
    return customer_data

def add_customer_to_file(username):
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

    with open(CUSTOMER_INVENTORY_FILE, 'w') as inv_file:
        inv_file.append(new_customer_profile)

def new_customer():
    ''' New customer flow '''
    tprint('Welcome!')
    username = input('Please enter a username: ')
    
    add_customer_to_file(username)

    print("#############################################################################")
    print("########                                                             ########")
    print("########                   Self Service Portal                       ########")
    print("######## ----------------------------------------------------------- ########")
    print("########                       Hello, %s!                            ########"%username)
    print("########  Would you like to deploy a test or production environment? ########")
    print("########      You can alway add or remove an environment later       ########")
    print("######## ----------------------------------------------------------- ########")
    print("########                                                             ########")
    print("########                         Choose:                             ########")
    print("########                                                             ########")
    print("########      1) Test environment  |  2) Production environment      ########")
    print("########      3) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Choose a number between 1 and 3: ")



    
    

    return

def find_available_customer_number():
    ''' Find next available customer number '''
    customer_data = load_customer_data()
        
    customer_numbers = []
    for customer in customer_data:
        customer_numbers.append(customer['customer_number'])
    
    return max(customer_numbers)

def existing_customer_menu():
    ''' Existing customer menu '''


def alter_deployment():
    return

def modify_vagrantfile():
    return

if __name__ == '__main__':
    ''' Python script main function '''
    
    menu()
