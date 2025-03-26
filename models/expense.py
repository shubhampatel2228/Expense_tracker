# models/expense.py

from datetime import datetime

class Expense:
    def __init__(self, name, category, amount, date=None):
        self.name = name
        self.category = category
        self.amount = amount
        self.date = date if date else datetime.today()

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "amount": self.amount,
            "date": self.date.strftime("%Y-%m-%d")
        }

    @staticmethod
    def from_dict(data):
        name = data.get("name", "")
        category = data.get("category", "")
        amount = float(data.get("amount", 0.0))
        date_str = data.get("date", datetime.today().strftime("%Y-%m-%d"))
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return Expense(name, category, amount, date)
