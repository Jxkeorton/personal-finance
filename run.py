import gspread
from google.oauth2.service_account import Credentials

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

    choice = input("Please select an option (1-2): ")
    
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
    
    choice = input("Please select an option (1-2): ")
    
    if choice == 1:
        new_transaction_menu()
    elif choice == 2:
        monthly_budget()
    
def new_transaction_menu():
    '''
    Displays available transaction options
    '''

def monthly_budget():
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

    choice = input("Please select an option (1-2): ")

    if choice == 1:
        income_report()
    elif choice == 2:
        expense_report()
    elif choice == 3:
        summary()
    elif choice == 4:
        analytics()

def income_report():
    '''
    Displays income report
    '''

def expense_report():
    '''
    Displays expense report
    '''

def summary():
    '''
    Displays monthly summary
    '''

def analytics():
    '''
    Displays analytics of spending activity
    '''
    
def main():
    '''
    Run all functions in program
    '''
    main_menu()

if __name__ == '__main__':
    main()