class Expense:
    def __init__(self, expense_id, date, amount, category, description):
        self.expense_id = expense_id
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def display(self):
        print(f"ID: {self.expense_id}")
        print(f"Date: {self.date}")
        print(f"Amount: ₹{self.amount}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")

