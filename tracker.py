# tracker.py

import os
import json
import csv
from datetime import datetime
from models.expense import Expense
from models.budget import Budget
from utils.file_handler import load_data, save_data

DATA_FILE = 'data/expenses.json'
LOG_FILE = 'data/transactions.log'  # ✅ Log file for raw transactions

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budget = Budget()
        self.load()

    def load(self):
        data = load_data(DATA_FILE)
        self.expenses = [Expense.from_dict(e) for e in data.get("expenses", [])]
        self.budget.from_dict(data.get("budget", {}))

    def save(self):
        data = {
            "expenses": [e.to_dict() for e in self.expenses],
            "budget": self.budget.to_dict()
        }
        save_data(DATA_FILE, data)

    def log_transaction(self, expense):
        """✅ Log each transaction to a separate text file."""
        with open(LOG_FILE, "a") as f:
            f.write(f"{expense.date.strftime('%Y-%m-%d')} | {expense.category:<12} | {expense.name:<20} | ${expense.amount:.2f}\n")

    def add_expense(self):
        try:
            name = input("Expense name: ")
            category = input("Category (e.g., Food, Transport): ")
            amount = float(input("Amount: "))
            date_str = input("Date (YYYY-MM-DD, leave blank for today): ")
            date = datetime.strptime(date_str, "%Y-%m-%d") if date_str else datetime.today()

            expense = Expense(name, category, amount, date)
            self.expenses.append(expense)
            self.log_transaction(expense)  # ✅ Log to .log file
            self.save()
            print("✅ Expense added successfully.")
        except Exception as e:
            print(f"❌ Error adding expense: {e}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\n--- All Expenses ---")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e.date.date()} | {e.category} | {e.name} - ${e.amount:.2f}")

    def view_expenses_by_month(self):
        month_str = input("Enter month (YYYY-MM): ").strip()
        try:
            print(f"\n--- Expenses for {month_str} ---")
            found = False
            for idx, e in enumerate(self.expenses, 1):
                if e.date.strftime("%Y-%m") == month_str:
                    print(f"{idx}. {e.date.date()} | {e.category} | {e.name} - ${e.amount:.2f}")
                    found = True
            if not found:
                print("No expenses found for this month.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def set_budget(self):
        try:
            category = input("Category to set budget for: ")
            amount = float(input("Budget amount: "))
            self.budget.set_category_budget(category, amount)
            self.save()
            print("✅ Budget set successfully.")
        except Exception as e:
            print(f"❌ Error setting budget: {e}")

    def view_budget_summary(self):
        summary = self.budget.get_summary(self.expenses)
        print("\n--- Budget Summary ---")
        for category, data in summary.items():
            print(f"{category}: Spent ${data['spent']:.2f} / Budget ${data['budget']:.2f}")

    def export_to_csv(self, filename="expenses_export.csv"):
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Category", "Name", "Amount"])
                for e in self.expenses:
                    writer.writerow([e.date.date(), e.category, e.name, f"{e.amount:.2f}"])
            print(f"✅ Exported to {filename}")
        except Exception as e:
            print(f"❌ Error exporting to CSV: {e}")
