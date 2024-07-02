import sys
from utils import clear_terminal
from options import OptionsMenu
from reports import ReportsMenu


class MainMenu:
    def __init__(self):
        self.options_menu = OptionsMenu(main_menu=self)
        self.reports_menu = ReportsMenu(main_menu=self)

    def display(self):
        """
        Displays the main menu to the user and handles their input.

        The menu presents three options to the user:
        1. Options - Navigates to the Options menu.
        2. Reports - Navigates to the Reports menu.
        3. Exit - Exits the program.

        The method clears the terminal, displays the menu options, and then
        waits for the user to input their choice. If the input is invalid
        (i.e., not an integer between 1 and 3), it prompts the user to
        re-enter their choice. Based on the user's selection, the method
        either calls the display method of the corresponding menu (Options
        or Reports) or exits the program.
        """
        clear_terminal()
        menu_list = ["Options", "Reports", "Exit"]
        print("HOME")
        for i, option in enumerate(menu_list, start=1):
            print(f"{i}. {option}")

        while True:
            try:
                choice = int(input("Please select an option (1-3): "))
                if choice not in range(1, 4):
                    raise ValueError("Choice out of range.")
                break
            except ValueError:
                print("Invalid choice. Please enter 1, 2 or 3.")

        if choice == 1:
            self.options_menu.display()
        elif choice == 2:
            self.reports_menu.display()
        elif choice == 3:
            sys.exit("Exiting the program.")
