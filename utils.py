import os
from datetime import datetime
import sys


def clear_terminal():
    '''
    Clear terminal based on platform
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def prompt_user_to_continue():
    '''
    Prompts the user to choose how they would like to continue
    '''
    from menus import MainMenu  # Deferred import to avoid circular import
    print("\nChoose option 1 or 2 to continue")
    print("1: Main menu")
    print("2: Exit")
    while True:
        user_input = input("Please enter option 1 or 2: ")
        if user_input == '1':
            MainMenu().display()
            break
        elif user_input == '2':
            sys.exit("Exiting the program.")
        else:
            print("Invalid input. Enter 1 or 2 ")


def parse_date(date_str):
    '''
    Parse date string into datetime object
    '''
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj
    except ValueError:
        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
        return None
