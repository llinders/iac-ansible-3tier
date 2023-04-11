import vagrant
import os
import sys
from fabric.api import *

from portal.menu.menu_navigation import Menu, show_menu

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

def new_customer():
    ''' New customer flow '''
    

def existing_customer_menu():
    ''' Existing customer menu '''


def modify_vagrantfile():
    return

if __name__ == '__main__':
    ''' Python script main function '''
    startup_menu()
