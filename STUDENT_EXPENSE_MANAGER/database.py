import csv
import os

FILE_NAME = "expenses.csv"

FIELDS = [
    "id",
    "date",
    "category",
    "description",
    "amount"
]


def initialize_database():
    """Create expenses.csv if it does not exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def load_expenses():
    """Load all expenses from CSV file."""
    initialize_database()

    expenses = []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append({
                "id": int(row["id"]),
                "date": row["date"],
                "category": row["category"],
                "description": row["description"],
                "amount": float(row["amount"])
            })

    return expenses


def save_expenses(expenses):
    """Save all expenses to CSV file."""
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()

        for expense in expenses:
            writer.writerow(expense)


def get_next_id(expenses):
    """Generate the next expense ID."""
    if not expenses:
        return 1

    return max(expense["id"] for expense in expenses) + 1
