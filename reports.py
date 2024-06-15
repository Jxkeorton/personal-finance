import sys
from utils import clear_terminal, prompt_user_to_continue, parse_date
from tabulate import tabulate
from datetime import datetime, timedelta
from sheet import SHEET


class ReportsMenu:
    def display(self):
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
                print("Invalid choice. Enter either 1, 2, 3, 4, 5 or 6.")

        if choice == 1:
            self.transaction_report('income')
        elif choice == 2:
            self.transaction_report('expense')
        elif choice == 3:
            self.summary_report()
        elif choice == 4:
            self.analytics_report()
        elif choice == 5:
            self.display()
        elif choice == 6:
            sys.exit("Exiting the program.")

    def transaction_report(self, transaction_type):
        clear_terminal()
        print(f"{transaction_type.upper()} REPORT")
        print("Please enter the date range in YYYY-MM-DD format.\n")

        while True:
            start_date_str = input("Enter start date (YYYY-MM-DD): ")
            start_date = parse_date(start_date_str)
            if start_date is None:
                print("Invalid date format. Please try again.")
                continue

            end_date_str = input("Enter end date (YYYY-MM-DD): ")
            end_date = parse_date(end_date_str)
            if end_date is None:
                print("Invalid date format. Please try again.")
                continue

            if start_date > end_date:
                print("Start date must precede or equal end date. Try again.")
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
            message = (f"No {transaction_type} transactions \
                        found between {start_date_str} and {end_date_str}.")
            print(message)

        prompt_user_to_continue()

    def summary_report(self):
        from sheet import SHEET
        clear_terminal()
        print("MONTHLY SUMMARY REPORT")

        today = datetime.now()
        first_day_of_current_month = today.replace(day=1)
        last_day_of_previous_month = (
            first_day_of_current_month - timedelta(days=1)
            )
        first_day_of_previous_month = last_day_of_previous_month.replace(day=1)

        income_worksheet = SHEET.worksheet('income')
        income_transactions = income_worksheet.get_all_records()

        expense_worksheet = SHEET.worksheet('expense')
        expense_transactions = expense_worksheet.get_all_records()

        previous_month_income = sum(
            float(transaction['amount'])
            for transaction in income_transactions
            if first_day_of_previous_month <=
            parse_date(transaction['date']) <=
            last_day_of_previous_month
        )

        previous_month_expense = sum(
            float(transaction['amount'])
            for transaction in expense_transactions
            if first_day_of_previous_month <=
            parse_date(transaction['date']) <=
            last_day_of_previous_month
        )

        print(f"Month: {first_day_of_previous_month.strftime('%B %Y')}")
        data = [
            ["Total Income", previous_month_income],
            ["Total Expense", previous_month_expense],
            ["Net", previous_month_income - previous_month_expense]
        ]
        print(tabulate(data, headers=["Category", "Amount"]))

        prompt_user_to_continue()

    def analytics_report(self):
        from sheet import SHEET
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
                print("Start date must precede or equal \
                       end date. Please try again.")
                continue

            break

        expense_transactions = SHEET.worksheet('expense').get_all_records()

        total_spending = sum(
            float(transaction['amount'])
            for transaction in expense_transactions
            if start_date <=
            parse_date(transaction['date']) <=
            end_date
        )

        categories = set(
            transaction['category'] for transaction in expense_transactions
        )
        spending_by_category = {
            category: sum(
                float(transaction['amount'])
                for transaction in expense_transactions
                if transaction['category'] == category and start_date <=
                parse_date(transaction['date']) <= end_date
            )
            for category in categories
        }

        data = []
        for category, amount in spending_by_category.items():
            data.append([category, amount])

        print(tabulate(data, headers=['Category', 'Amount']))
        print("--------------")
        print(f"Total Spending: {total_spending}")

        prompt_user_to_continue()
