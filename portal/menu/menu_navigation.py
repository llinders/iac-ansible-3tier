from enum import Enum

class Menu(Enum):
    STARTUP_MENU = 1
    NEW_CUSTOMER = 2
    EXISTING_CUSTOMER = 3



def show_menu(menu, username='user'):
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
                    show_menu(Menu.EXISTING_CUSTOMER)
                case _:
                    print('You have to enter a value between 1 and 3')
                
        case Menu.NEW_CUSTOMER:
            print('d')
        case _:
            raise ValueError('Not a valid menu')
        