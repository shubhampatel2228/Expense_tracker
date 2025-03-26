# main.py

from tracker import ExpenseTracker
from utils.report_generator import ReportGenerator

def print_menu():
    print("\n=== CLI Budget Buddy ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Set Monthly Budget")
    print("4. View Budget Summary")
    print("5. Generate Report")
    print("6. Export Data to CSV")
    print("7. Exit")

def main():
    tracker = ExpenseTracker()
    report_gen = ReportGenerator(tracker)

    while True:
        print_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.set_budget()
        elif choice == '4':
            tracker.view_budget_summary()
        elif choice == '5':
            report_gen.generate_report()
        elif choice == '6':
            tracker.export_to_csv()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
