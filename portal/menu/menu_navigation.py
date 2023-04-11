import os
from enum import Enum
from art import tprint

import data.customer_data_utils as cdu
import deployment.environment_manager as em

class Menu(Enum):
    '''Enum class that contains all menu options for the CLI'''
    STARTUP_MENU = 1
    NEW_CUSTOMER = 2
    LOGIN = 3
    LOGIN_FAILED = 4
    EXISTING_CUSTOMER = 5


def show_menu(menu, username='user', customer_number=None):
    INVALID_INPUT_MSG = 'Please enter a valid input number'

    _clear_screen()
    match menu:
        case Menu.STARTUP_MENU:
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

            match chosen_element:
                case 1:
                    show_menu(Menu.NEW_CUSTOMER)
                case 2:
                    show_menu(Menu.LOGIN)
                case 3:
                    print('exit')
                case _:
                    print(INVALID_INPUT_MSG)
                
        case Menu.NEW_CUSTOMER:
            tprint('Welcome!')
            username = input('Please enter a username: ')
            
            cdu.write_new_customer(username)

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

            match chosen_element:
                case 1:
                    em.deploy_new_test_environment()
                case 2: 
                    em.deploy_new_prod_environment()
                case 3:
                    print('exit')
                case _:
                    print(INVALID_INPUT_MSG)
        
        case Menu.LOGIN:
            tprint('Welcome back!')
            customer_number = input('Please enter your customer number to login: ')

            if (cdu.check_if_exists(customer_number)):
                show_menu(Menu.EXISTING_CUSTOMER, username, customer_number)
            else:
                show_menu(Menu.LOGIN_FAILED)
        
        case Menu.LOGIN_FAILED:
            print("#############################################################################")
            print("########                                                             ########")
            print("########                   Self Service Portal                       ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                       LOGIN FAILED                          ########")
            print("########       Would you like to try again or exit to main menu?     ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                         Choose:                             ########")
            print("########                                                             ########")
            print("########              1) Try again  |  2) Back to main menu          ########")
            print("########                                                             ########")
            print("########                                                             ########")
            print("#############################################################################")
            chosen_element = input("Choose a number between 1 and 2: ")

            match chosen_element:
                case 1:
                    show_menu(Menu.LOGIN)
                case 2:
                    show_menu(Menu.STARTUP_MENU)
                case _:
                    print(INVALID_INPUT_MSG)

        case Menu.EXISTING_CUSTOMER:
            print("#############################################################################")
            print("########                                                             ########")
            print("########                   Self Service Portal                       ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                     Welcome back, %s!                       ########"%username)
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
           
            customer_info = cdu.get_customer(customer_number)
            test_env = customer_info['test_env_setup']
            prod_env = customer_info['prod_env_setup']
            
            print('                 ## Information about current deployment ##')
            print('Test environment:')
            if test_env['deployed'] == False: print('\t' + 'NOT DEPLOYED')
            else:
                for item in test_env:
                    print('\t%s:\t\t%s'%(item.replace('_ip', ''), test_env.get(item)))
            
            print('Production environment:')
            
            for item in prod_env:
                if (item != 'webservers'):
                    print('\t%s:\t\t%s'%(item.replace('_ip', ''), prod_env.get(item)))
                else:
                    print('\t' + 'webservers:')
                    for server in prod_env['webservers']:
                        print('\t\t%s:\t%s'%(server.replace('_ip', ''), prod_env.get('webservers').get(server)))
                
        case _:
            raise ValueError('Not a valid menu')
            

def _clear_screen():
    os.system('cls||clear')
