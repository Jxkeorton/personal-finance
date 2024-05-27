import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

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

def main_menu():
    '''
    Display the main menu within terminal
    '''
    menu_list = [
        "Options",
        "Reports"
    ]

    print("HOME")
    for i, option in enumerate(menu_list, start=1):
        print(f"{i}. {option}")

    choice = int(input("Please select an option (1-2): "))
    
    if choice == 1:
        options_menu()
    elif choice == 2:
        reports_menu()
    
def options_menu():
    '''
    Displays list of options available
    '''

    list = [
        "New Transaction",
        "Edit Monthly Budget"
    ]

    print("OPTIONS")
    for i, option in enumerate(list, start=1):
        print(f"{i}. {option}")
    
    choice = int(input("Please select an option (1-2): "))
    
    if choice == 1:
        new_transaction_menu()
    elif choice == 2:
        edit_monthly_budget()
    
def new_transaction_menu():
    '''
    Displays available transaction options
    '''

    list = [
        "Add Income",
        "Add Expense"
    ]

    print("NEW TRANSACTION")
    for i, option in enumerate(list, start=1):
        print(f"{i}. {option}")
    
    choice = int(input("Please select an option (1-2): "))
    if choice == 1:
        add_transaction("income")
    elif choice == 2:
        add_transaction("expense")

def add_transaction(transaction_type):
    '''
    Allows user to add a new transaction (income or expense) and choose a category
    '''
    print(f"ADD {transaction_type.upper()}")
    print("Enter numbers only\n")

    while True:
        try:
            amount = float(input(f"Enter a new {transaction_type} amount here: "))
            if amount < 0:
                print("Amount must be positive. Please try again.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")
    
    category = input(f"Enter a category for the {transaction_type}: ")
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    print(f"Updating {transaction_type} worksheet...")
    worksheet_to_update = SHEET.worksheet(transaction_type)
    worksheet_to_update.append_row([amount, category, current_date])
    print(f"{transaction_type.capitalize()} entry added successfully!")
    print(f"Amount: {amount}, Category: {category}, Date: {current_date}\n")

def edit_monthly_budget():
    '''
    Allows user to edit there monthly budget
    '''
    print("EDIT YOUR MONTHLY BUDGET")

    stats = SHEET.worksheet('stats')
    current_budget = stats.col_values(2)[1]
    if current_budget == 0:
        print("You dont currently have a monthly budget set\n")
    else:
        print(f"Current monthly budget: {current_budget}\n")

    while True:
        try:
            new_monthly_budget = float(input("Please add a new monthly budget: "))
            if new_monthly_budget < 0:
                print("Amount must be positive. Please try again.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")
    
    print("Updating monthly budget...")
    stats.update_cell(2, 2, new_monthly_budget)
    print(f"Current budget updated to: {new_monthly_budget}")
    
def reports_menu():
    '''
    Displays list of reports available
    '''

    list = [
        "Income",
        "Expenses",
        "Summary",
        "Analytics"
    ]

    print("REPORTS")
    for i, option in enumerate(list, start=1):
        print(f"{i}. {option}")

    choice = int(input("Please select an option (1-4): "))

    if choice == 1:
        income_report()
    elif choice == 2:
        expense_report()
    elif choice == 3:
        summary_report()
    elif choice == 4:
        analytics_report()

def income_report():
    '''
    Displays income report within the specified range
    '''
    print("INCOME REPORT")
    print("Please enter the date range in YYYY-MM-DD format.\n")

    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")

    start_date = parse_date(start_date_str)
    end_date = parse_date(end_date_str)

    if not start_date or not end_date:
        print("Invalid date format. Please try again.")
        return

    if start_date > end_date:
        print("Start date must be earlier than or equal to end date. Please try again.")
        return
    
    worksheet = SHEET.worksheet('income')
    transactions = worksheet.get_all_records()

    filtered_transactions = []
    total_income = 0.0

    for transaction in transactions:
        transaction_date = parse_date(transaction['date'])
        if start_date <= transaction_date <= end_date:
            filtered_transactions.append(transaction)
            total_income += float(transaction['amount'])
    
    if not filtered_transactions:
        print(f"No income transactions found between {start_date_str} and {end_date_str}.")
    else:
        print(f"Income transactions between {start_date_str} and {end_date_str}:")
        for transaction in filtered_transactions:
            print(f"Date: {transaction['date']}, Amount: {transaction['amount']}, Category: {transaction['category']}")
        print(f"\nTotal Income: {total_income}")

def expense_report():
    '''
    Displays expense report within the specified range
    '''
    print("EXPENSE REPORT")
    print("Please enter the date range in YYYY-MM-DD format.\n")

    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")

    start_date = parse_date(start_date_str)
    end_date = parse_date(end_date_str)

    if not start_date or not end_date:
        print("Invalid date format. Please try again.")
        return

    if start_date > end_date:
        print("Start date must be earlier than or equal to end date. Please try again.")
        return

    worksheet = SHEET.worksheet('expense')
    transactions = worksheet.get_all_records()

    filtered_transactions = []
    total_expense = 0.0

    for transaction in transactions:
        transaction_date = parse_date(transaction['date'])
        if start_date <= transaction_date <= end_date:
            filtered_transactions.append(transaction)
            total_expense += float(transaction['amount'])

    if not filtered_transactions:
        print(f"No expense transactions found between {start_date_str} and {end_date_str}.")
    else:
        print(f"Expense transactions between {start_date_str} and {end_date_str}:")
        for transaction in filtered_transactions:
            print(f"Date: {transaction['date']}, Amount: {transaction['amount']}, Category: {transaction['category']}")
        print(f"\nTotal Expense: {total_expense}")


def parse_date(date_str):
    '''
    Parse date string into datetime object
    '''
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None

def summary_report():
    '''
    Displays monthly summary
    '''

def analytics_report():
    '''
    Displays analytics of spending activity
    '''
    
def main():
    '''
    Run all functions in program
    '''
    main_menu()

if __name__ == '__main__':
    # main()
    income_report()