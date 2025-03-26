# utils/report_generator.py

from collections import defaultdict
from datetime import datetime
from termcolor import colored

class ReportGenerator:
    def __init__(self, tracker):
        self.tracker = tracker

    def generate_report(self):
        print("\n=== Monthly Spending Report ===")
        expenses = self.tracker.expenses
        if not expenses:
            print("No expenses to report.")
            return

        monthly_totals = defaultdict(float)
        category_totals = defaultdict(float)

        for e in expenses:
            month = e.date.strftime("%Y-%m")
            monthly_totals[month] += e.amount
            category_totals[e.category] += e.amount

        print("\n--- Spending by Month ---")
        for month, total in sorted(monthly_totals.items()):
            print(f"{month}: ${total:.2f}")

        print("\n--- Spending by Category ---")
        for cat, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            color = "green" if total < 100 else "yellow" if total < 300 else "red"
            print(f"{cat}: {colored(f'${total:.2f}', color)}")

        top_category = max(category_totals.items(), key=lambda x: x[1], default=None)
        if top_category:
            print(f"\n⚡ Top Spending Category: {top_category[0]} (${top_category[1]:.2f})")

        print("\n✅ Report generated successfully.")
