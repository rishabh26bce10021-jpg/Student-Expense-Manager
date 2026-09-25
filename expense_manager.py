from expense import Expense
from storage import save_expenses, load_expenses


class ExpenseManager:

    def __init__(self):
        self.expenses = []

        saved_data = load_expenses()

        for item in saved_data:
            expense = Expense(
                item["id"],
                item["date"],
                item["amount"],
                item["category"],
                item["description"]
            )

            self.expenses.append(expense)

    def add_expense(self, date, amount, category, description):
        expense_id = len(self.expenses) + 1

        new_expense = Expense(
            expense_id,
            date,
            amount,
            category,
            description
        )

        self.expenses.append(new_expense)

        save_expenses(self.expenses)

        print("\nExpense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses found.")
            return

        print("\n========== ALL EXPENSES ==========")

        for expense in self.expenses:
            expense.display()
            print("----------------------------------")

    def search_by_category(self, category):
        results = []

        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                results.append(expense)

        return results

    def search_by_date(self, date):
        results = []

        for expense in self.expenses:
            if expense.date == date:
                results.append(expense)

        return results

    def search_by_amount(self, amount):
        results = []

        for expense in self.expenses:
            if expense.amount == amount:
                results.append(expense)

        return results

    def edit_expense(self, expense_id, date, amount, category, description):
        for expense in self.expenses:

            if expense.expense_id == expense_id:
                expense.date = date
                expense.amount = amount
                expense.category = category
                expense.description = description

                save_expenses(self.expenses)

                return True

        return False

    def delete_expense(self, expense_id):
        for expense in self.expenses:

            if expense.expense_id == expense_id:
                self.expenses.remove(expense)

                save_expenses(self.expenses)

                return True

        return False