import sys
from utils import clear_terminal, prompt_user_to_continue
from colorama import Back, Style
from transactions import TransactionMenu
from sheet import SHEET


class OptionsMenu:
    def __init__(self):
        self.transaction_menu = TransactionMenu()

    def display(self):
        clear_terminal()
        list = ["New Transaction", "Edit Monthly Budget", "Main menu", "Exit"]
        print("OPTIONS")
        for i, option in enumerate(list, start=1):
            print(f"{i}. {option}")

        while True:
            try:
                choice = int(input("Please select an option (1-4): "))
                if choice not in range(1, 5):
                    raise ValueError("Choice out of range.")
                break
            except ValueError:
                print("Invalid choice. Please enter 1, 2, 3 or 4.")

        if choice == 1:
            self.transaction_menu.display()
        elif choice == 2:
            self.edit_monthly_budget()
        elif choice == 3:
            self.display()
        elif choice == 4:
            sys.exit("Exiting the program.")

    def edit_monthly_budget(self):
        clear_terminal()
        print("EDIT YOUR MONTHLY BUDGET")
        print("Loading current monthly budget...\n")

        stats = SHEET.worksheet('stats')
        current_budget = stats.col_values(2)[1]
        if current_budget == 0:
            print("You don't currently have a monthly budget set\n")
        else:
            print(f"Current monthly budget: {current_budget}\n")

        while True:
            try:
                prompt = "Please enter a new monthly budget: "
                new_monthly_budget = float(input(prompt))
                if new_monthly_budget < 0:
                    print("Amount must be positive. Please try again.\n")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.\n")

        print("Updating monthly budget...\n")
        stats.update_cell(2, 2, new_monthly_budget)
        message = f"Current budget updated to: {new_monthly_budget}"
        print(Back.GREEN + message + Style.RESET_ALL)

        prompt_user_to_continue()
