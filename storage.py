import json
import os

FILE_PATH = "data/expenses.json"


def save_expenses(expenses):
    data = []

    for expense in expenses:
        data.append({
            "id": expense.expense_id,
            "date": expense.date,
            "amount": expense.amount,
            "category": expense.category,
            "description": expense.description
        })

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def load_expenses():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        return json.load(file)