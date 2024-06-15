from utils import clear_terminal, prompt_user_to_continue
from sheet import SHEET
from datetime import datetime
from colorama import Back, Style
import sys


class TransactionMenu:
    def __init__(self, main_menu):
        self.main_menu = main_menu

    def display(self):
        clear_terminal()
        list = ["Add Income", "Add Expense", "Go Back", "Exit"]
        print("NEW TRANSACTION")
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
            self.add_transaction("income")
        elif choice == 2:
            self.add_transaction("expense")
        elif choice == 3:
            self.main_menu.display()
        elif choice == 4:
            sys.exit("Exiting the program.")

    def add_transaction(self, transaction_type):
        clear_terminal()
        print(f"ADD {transaction_type.upper()}")
        print("Enter numbers only\n")

        while True:
            try:
                prompt = f"Enter a new {transaction_type} amount here: "
                amount = float(input(prompt))
                if amount < 0:
                    print("Amount must be positive. Please try again.\n")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.\n")

        while True:
            category = input(f"Enter a category for the {transaction_type}: ")
            if not category.strip():
                print("Category cannot be empty. Please try again.")
                continue
            break

        current_date = datetime.now().strftime("%Y-%m-%d")

        print(f"Updating {transaction_type} worksheet...")
        worksheet_to_update = SHEET.worksheet(transaction_type)
        worksheet_to_update.append_row([amount, category, current_date])
        message = f"{transaction_type.capitalize()} entry added successfully!"
        print(Back.GREEN + message + Style.RESET_ALL)
        print(f"Amount: {amount}, Category: {category},\
               Date: {current_date}\n")

        prompt_user_to_continue()
