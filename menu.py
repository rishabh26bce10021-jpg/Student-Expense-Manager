from expense_manager import ExpenseManager
from validation import (
    validate_amount,
    validate_date,
    validate_category,
    validate_description
)
from reports import show_report


def show_menu():
    manager = ExpenseManager()

    while True:
        print("\n========================================")
        print("       STUDENT EXPENSE MANAGER")
        print("========================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search / Filter Expenses")
        print("4. Edit Expense")
        print("5. Delete Expense")
        print("6. Generate Report")
        print("7. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense_menu(manager)

        elif choice == "2":
            manager.view_expenses()

        elif choice == "3":
            search_expense_menu(manager)

        elif choice == "4":
            edit_expense_menu(manager)

        elif choice == "5":
            delete_expense_menu(manager)

        elif choice == "6":
            show_report(manager.expenses)

        elif choice == "7":
            print("\nThank you for using Student Expense Manager!")
            break

        else:
            print("\nInvalid choice. Please try again.")


def add_expense_menu(manager):

    print("\n========== ADD EXPENSE ==========")

    date = input("Enter date (DD-MM-YYYY): ")

    valid, date_result = validate_date(date)

    if not valid:
        print(date_result)
        return

    amount = input("Enter amount: ")

    valid, amount_result = validate_amount(amount)

    if not valid:
        print(amount_result)
        return

    category = input("Enter category: ")

    valid, category_result = validate_category(category)

    if not valid:
        print(category_result)
        return

    description = input("Enter description: ")

    valid, description_result = validate_description(description)

    if not valid:
        print(description_result)
        return

    manager.add_expense(
        date_result,
        amount_result,
        category_result,
        description_result
    )


def search_expense_menu(manager):

    print("\n========== SEARCH EXPENSE ==========")
    print("1. Search by Category")
    print("2. Search by Date")
    print("3. Search by Amount")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ")
        results = manager.search_by_category(category)

    elif choice == "2":
        date = input("Enter date (DD-MM-YYYY): ")
        results = manager.search_by_date(date)

    elif choice == "3":
        amount = input("Enter amount: ")

        valid, amount_result = validate_amount(amount)

        if not valid:
            print(amount_result)
            return

        results = manager.search_by_amount(amount_result)

    else:
        print("\nInvalid choice.")
        return

    if not results:
        print("\nNo matching expenses found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for expense in results:
        expense.display()
        print("----------------------------------")


def edit_expense_menu(manager):

    print("\n========== EDIT EXPENSE ==========")

    try:
        expense_id = int(input("Enter expense ID to edit: "))
    except ValueError:
        print("\nPlease enter a valid ID.")
        return

    date = input("Enter new date (DD-MM-YYYY): ")
    valid, date_result = validate_date(date)

    if not valid:
        print(date_result)
        return

    amount = input("Enter new amount: ")
    valid, amount_result = validate_amount(amount)

    if not valid:
        print(amount_result)
        return

    category = input("Enter new category: ")
    valid, category_result = validate_category(category)

    if not valid:
        print(category_result)
        return

    description = input("Enter new description: ")
    valid, description_result = validate_description(description)

    if not valid:
        print(description_result)
        return

    success = manager.edit_expense(
        expense_id,
        date_result,
        amount_result,
        category_result,
        description_result
    )

    if success:
        print("\nExpense updated successfully!")
    else:
        print("\nExpense ID not found.")


def delete_expense_menu(manager):

    print("\n========== DELETE EXPENSE ==========")

    try:
        expense_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("\nPlease enter a valid ID.")
        return

    success = manager.delete_expense(expense_id)

    if success:
        print("\nExpense deleted successfully!")
    else:
        print("\nExpense ID not found.")