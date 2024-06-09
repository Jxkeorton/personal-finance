import os
import sys
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta
from tabulate import tabulate
from colorama import Back, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('personal_finance')

stats = SHEET.worksheet('stats')
data = stats.get_all_values()


def clear_terminal():
    # Clear terminal based on platform
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    '''
    Display the main menu within terminal
    '''

    clear_terminal()

    menu_list = [
        "Options",
        "Reports",
        "Exit"
    ]

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
        options_menu()
    elif choice == 2:
        reports_menu()
    elif choice == 3:
        sys.exit("Exiting the program.")



def options_menu():
    '''
    Displays list of options available
    '''

    clear_terminal()

    list = [
        "New Transaction",
        "Edit Monthly Budget",
        "Main menu",
        "Exit"
    ]

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
        new_transaction_menu()
    elif choice == 2:
        edit_monthly_budget()
    elif choice == 3:
        main_menu()
    elif choice == 4:
        sys.exit("Exiting the program.")


def new_transaction_menu():
    '''
    Displays available transaction options
    '''

    clear_terminal()

    list = [
        "Add Income",
        "Add Expense",
        "Main Menu",
        "Exit"
    ]

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
        add_transaction("income")
    elif choice == 2:
        add_transaction("expense")
    elif choice == 3:
        main_menu()
    elif choice == 4:
        sys.exit("Exiting the program.")


def add_transaction(transaction_type):
    '''
    Allows user to add a new transaction
    (income or expense) and choose a category
    '''

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

    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    print(f"Updating {transaction_type} worksheet...")
    worksheet_to_update = SHEET.worksheet(transaction_type)
    worksheet_to_update.append_row([amount, category, current_date])
    message = f"{transaction_type.capitalize()} entry added successfully!"
    print(Back.GREEN + message + Style.RESET_ALL)
    print(f"Amount: {amount}, Category: {category}, Date: {current_date}\n")

    prompt_user_to_continue()


def edit_monthly_budget():
    '''
    Allows user to edit there monthly budget
    '''

    clear_terminal()

    print("EDIT YOUR MONTHLY BUDGET")

    stats = SHEET.worksheet('stats')
    current_budget = stats.col_values(2)[1]
    if current_budget == 0:
        print("You dont currently have a monthly budget set\n")
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


def reports_menu():
    '''
    Displays list of reports available
    '''

    clear_terminal()

    list = [
        "Income",
        "Expenses",
        "Summary",
        "Analytics",
        "Main Menu",
        "Exit"
    ]

    print("REPORTS")
    for i, option in enumerate(list, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Please select an option (1-6): "))
            if choice not in range(1, 7):
                raise ValueError("Choice out of range.")
            break
        except ValueError:
            print("Invalid choice. Please enter either 1, 2, 3, 4, 5 or 6.")

    if choice == 1:
        transaction_report('income')
    elif choice == 2:
        transaction_report('expense')
    elif choice == 3:
        summary_report()
    elif choice == 4:
        analytics_report()
    elif choice == 5:
        main_menu()
    elif choice == 6:
        sys.exit("Exiting the program.")


def transaction_report(transaction_type):
    '''
    Displays transaction report within the specified type and range
    '''

    clear_terminal()

    print(f"{transaction_type.upper()} REPORT")
    print("Please enter the date range in YYYY-MM-DD format.\n")

    while True:
        start_date_str = input("Enter start date (YYYY-MM-DD): ")
        end_date_str = input("Enter end date (YYYY-MM-DD): ")

        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)

        if start_date is None or end_date is None:
            print("Invalid date format. Please try again.")
            continue

        if start_date > end_date:
            print("Start date must precede or equal end date. \
                  Please try again.")
            continue

        break

    worksheet = SHEET.worksheet(transaction_type)
    transactions = worksheet.get_all_records()

    filtered_transactions = []
    total_income = 0.0

    for transaction in transactions:
        transaction_date = parse_date(transaction['date'])
        if start_date <= transaction_date <= end_date:
            filtered_transactions.append(transaction)
            total_income += float(transaction['amount'])

    table = []
    for transaction in filtered_transactions:
        table.append([
            transaction['date'],
            transaction['amount'],
            transaction['category']
        ])
    if table:
        print(tabulate(table, headers=['Date', 'Amount', 'Category']))
        print(f"\nTotal {transaction_type.capitalize()}: {total_income}")
    else:
        message = (f"No {transaction_type} transactions found between \
                   {start_date_str} and {end_date_str}.")
        print(message)

    prompt_user_to_continue()


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


def summary_report():
    '''
    Displays monthly summary for the previous month
    '''

    clear_terminal()

    print("MONTHLY SUMMARY REPORT")

    today = datetime.now()

    # Calculate start and end dates for the previous month
    first_day_of_current_month = today.replace(day=1)
    last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
    first_day_of_previous_month = last_day_of_previous_month.replace(day=1)

    income_worksheet = SHEET.worksheet('income')
    income_transactions = income_worksheet.get_all_records()

    expense_worksheet = SHEET.worksheet('expense')
    expense_transactions = expense_worksheet.get_all_records()

    # Filter income and expense transactions for the previous month
    previous_month_income = sum(
        float(transaction['amount']) for transaction in income_transactions
        if first_day_of_previous_month
        <= parse_date(transaction['date'])
        <= last_day_of_previous_month)

    previous_month_expense = sum(
        float(transaction['amount']) for transaction in expense_transactions
        if first_day_of_previous_month
        <= parse_date(transaction['date'])
        <= last_day_of_previous_month)

    print(f"Month: {first_day_of_previous_month.strftime('%B %Y')}")
    data = [
        ["Total Income", previous_month_income],
        ["Total Expense", previous_month_expense],
        ["Net", previous_month_income - previous_month_expense]
    ]
    print(tabulate(data, headers=["Category", "Amount"]))

    prompt_user_to_continue()


def analytics_report():
    '''
    Displays analytics of spending activity between start_date and end_date
    '''

    clear_terminal()

    print("SPENDING ANALYTICS REPORT")
    print("Please enter the date range in YYYY-MM-DD format.\n")

    while True:
        start_date_str = input("Enter start date (YYYY-MM-DD): ")
        end_date_str = input("Enter end date (YYYY-MM-DD): ")

        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)

        if start_date is None or end_date is None:
            print("Invalid date format. Please try again.")
            continue

        if start_date > end_date:
            print("Start date must precede or equal end date. \
                  Please try again.")
            continue

        break

    # Fetch income and expense transactions
    expense_transactions = SHEET.worksheet('expense').get_all_records()

    # Calculate total spending
    total_spending = sum(
        float(transaction['amount']) for transaction in expense_transactions
        if start_date
        <= parse_date(transaction['date'])
        <= end_date)

    # Calculate spending by category
    categories = set(
        transaction['category']
        for transaction in expense_transactions
    )
    spending_by_category = {category: sum(
        float(transaction['amount'])
        for transaction in expense_transactions
        if transaction['category'] == category and start_date
        <= parse_date(transaction['date'])
        <= end_date)
        for category in categories
    }

    data = []
    for category, amount in spending_by_category.items():
        data.append([category, amount])

    print(tabulate(data, headers=['Category', 'Amount']))
    print("--------------")
    print(f"Total Spending: {total_spending}")

    prompt_user_to_continue()


def prompt_user_to_continue():
    '''
    Prompts the user to press Enter to return to the main menu or Space bar to exit the script
    '''
    print("\nPress Enter to return to the main menu or Space bar to exit.")
    while True:
        user_input = input()
        if user_input == '':
            main_menu()
            break
        elif user_input == ' ':
            sys.exit("Exiting the program.")
        else:
            print("Invalid input. Press Enter to return to the main menu or Space bar to exit.")


def main():
    '''
    Run all functions in program
    '''
    main_menu()


if __name__ == '__main__':
    main()
