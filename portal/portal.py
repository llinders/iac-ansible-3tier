import vagrant
import os
import sys
from fabric.api import *
from art import tprint

from portal.menu.menu_navigation import Menu, show_menu
import data.customer_data_utils as customer_data_utils
import portal.deployment.environment_manager as env_manager

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

def startup_menu():
    ''' Main menu '''

    show_menu(Menu.STARTUP_MENU)

    chosen_element = input("Choose a number between 1 and 3: ")

    if int(chosen_element) == 1:
        new_customer()
    elif int(chosen_element) == 2:
        existing
    else:
        print('You have to enter a value between 1 and 3')



def new_customer():
    ''' New customer flow '''
    tprint('Welcome!')
    username = input('Please enter a username: ')
    
    customer_data_utils.write_new_customer(username)

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

    if (chosen_element == 1):
        env_manager.deploy_new_test_environment()

    return

def existing_customer_menu():
    ''' Existing customer menu '''


def modify_vagrantfile():
    return

if __name__ == '__main__':
    ''' Python script main function '''
    
    menu()
