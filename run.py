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

def expense_report():
    '''
    Displays expense report within the specified range
    '''

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
    new_transaction_menu()