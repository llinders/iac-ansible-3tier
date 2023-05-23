# from fabric.api import *

from menu.menu_navigation import Menu, show_menu

def startup_menu():
    ''' Main menu '''
    show_menu(Menu.STARTUP_MENU)

if __name__ == '__main__':
    ''' Python script main function '''
    startup_menu()
