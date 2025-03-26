# models/budget.py

class Budget:
    def __init__(self):
        self.category_limits = {}

    def set_category_budget(self, category, amount):
        self.category_limits[category] = amount

    def get_summary(self, expenses):
        summary = {}

        for category in self.category_limits:
            summary[category] = {
                "budget": self.category_limits[category],
                "spent": 0.0
            }

        for expense in expenses:
            cat = expense.category
            if cat in summary:
                summary[cat]["spent"] += expense.amount
            else:
                summary[cat] = {
                    "budget": 0.0,
                    "spent": expense.amount
                }

        return summary

    def to_dict(self):
        return self.category_limits

    def from_dict(self, data):
        if data:
            self.category_limits = data
