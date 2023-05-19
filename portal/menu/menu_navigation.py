import os
from enum import Enum
from art import tprint

import utils.data.customer_data_utils as cdu
import utils.deployment.environment_manager as em
from utils.customer_context_manager import CustomerContextManager


class Menu(Enum):
    '''Enum class that contains all menu options for the CLI'''
    STARTUP_MENU = 1
    NEW_CUSTOMER = 2
    LOGIN = 3
    LOGIN_FAILED = 4
    EXISTING_CUSTOMER = 5
    MANAGE_TEST_ENV = 6
    MANAGE_PROD_ENV = 7


def show_menu(menu: Menu, ccm: CustomerContextManager):
    INVALID_INPUT_MSG = "Please enter a valid input number"

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
            print("########       99) Exit                                              ########")
            print("########                                                             ########")
            print("#############################################################################")
            chosen_element = input("Choose a number between 1 and 3: ")

            match chosen_element:
                case 1:
                    show_menu(Menu.NEW_CUSTOMER, ccm)
                case 2:
                    show_menu(Menu.LOGIN, ccm)
                case 99:
                    print('exit')
                case _:
                    print(INVALID_INPUT_MSG)
                
        case Menu.NEW_CUSTOMER:
            tprint('Welcome!')
            username = input('Please enter a username: ')
            
            ccm.create_and_load_new_customer(username)

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
            print("########      99) Exit                                               ########")
            print("########                                                             ########")
            print("#############################################################################")
            chosen_element = input("Choose a number between 1 and 3: ")

            match chosen_element:
                case 1:
                    em.deploy_new_test_environment(ccm.get_customer_number())
                case 2: 
                    em.deploy_new_prod_environment(ccm.get_customer_number())
                case 99:
                    print('exit')
                case _:
                    print(INVALID_INPUT_MSG)
        
        case Menu.LOGIN:
            tprint('Welcome back!')
            customer_number = int(input('Please enter your customer number to login: '))

            try:
                ccm = CustomerContextManager(customer_number)
                show_menu(Menu.EXISTING_CUSTOMER, ccm)
            except:
                show_menu(Menu.LOGIN_FAILED, ccm)              
        
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
                    show_menu(Menu.LOGIN, ccm)
                case 2:
                    show_menu(Menu.STARTUP_MENU, ccm)
                case _:
                    print(INVALID_INPUT_MSG)

        case Menu.EXISTING_CUSTOMER:
            print("#############################################################################")
            print("########                                                             ########")
            print("########                   Self Service Portal                       ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                          Hi, %s!                       ########"%ccm.get_username())
            print("########     Choose to manage your test or production environment    ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                         Choose:                             ########")
            print("########                                                             ########")
            print("########             1) Manage test environment                      ########")
            print("########             2) Manage production environment                ########")
            print("########             99) Exit                                        ########")
            print("########                                                             ########")
            print("#############################################################################")
            _print_deployment_info(ccm.get_customer_number())

            chosen_element = input("Choose a number between 1 and 3: ")

            match chosen_element:
                case 1:
                    show_menu(Menu.MANAGE_TEST_ENV, ccm)
                case 2:
                    show_menu(Menu.MANAGE_PROD_ENV, ccm)
                case 99:
                    print('exit')
        
        case Menu.MANAGE_TEST_ENV:
            # 1. deploy 2. remove 3. go back
            print("#############################################################################")
            print("########                                                             ########")
            print("########                   Self Service Portal                       ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                Manage your test environment                 ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                         Choose:                             ########")
            print("########                                                             ########")
            print("########             1)  Deploy test environment                     ########")
            print("########             2)  Destroy test environment                    ########")
            print("########             99) Return to main menu                         ########")
            print("########                                                             ########")
            print("#############################################################################")

            chosen_element = input("Choose a number between 1 and 3: ")
            
            match chosen_element:
                case 1:
                    # deploy test if not exists
                    em.deploy_new_test_environment(ccm.get_customer_number())

                case 2:
                    # destroy test if exists
                    if (_confirmation_prompt()):
                        em.delete_test_environment(ccm.get_customer_number())
                    else:
                        print('Destruction cancled')
                        show_menu(Menu.MANAGE_TEST_ENV, ccm)
                    
                case 99:
                    show_menu(Menu.EXISTING_CUSTOMER, ccm)

        case Menu.MANAGE_PROD_ENV:
            # 1. deploy 2. Scale up/down 3. remove 4. go back 
            print("#############################################################################")
            print("########                                                             ########")
            print("########                   Self Service Portal                       ########")
            print("######## ----------------------------------------------------------- ########")
            print("########            Manage your production environment               ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                         Choose:                             ########")
            print("########                                                             ########")
            print("########      1)  Deploy prod environment                            ########")
            print("########      2)  Upscale or downscale existing prod environment     ########")
            print("########      3)  Destroy prod environment                           ########")
            print("########      99) Return to main menu                                ########")
            print("########                                                             ########")
            print("#############################################################################")

            chosen_element = input("Choose a number between 1 and 4: ")

 
        case _:
            raise ValueError('Not a valid menu')


def _print_deployment_info(customer_number) -> None:
    customer_info = cdu.get_customer(customer_number)
    test_env = customer_info['test_env_setup']
    prod_env = customer_info['prod_env_setup']
    
    print('                 ## Information about current deployment ##')
    print('Test environment:')
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
    
    print('')

def _confirmation_prompt() -> bool:
    answer = input("Please type 'y' or 'yes' to confirm, or 'no' to cancel")
    if answer.lower() in ["y","yes"]:
        return True
    else:
        return False

def _clear_screen() -> None:
    os.system('cls||clear')
