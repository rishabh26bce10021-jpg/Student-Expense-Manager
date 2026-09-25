def total_expense(expenses):
    total = 0

    for expense in expenses:
        total += expense.amount

    return total


def average_expense(expenses):
    if not expenses:
        return 0

    return total_expense(expenses) / len(expenses)


def highest_expense(expenses):
    if not expenses:
        return None

    highest = expenses[0]

    for expense in expenses:
        if expense.amount > highest.amount:
            highest = expense

    return highest


def lowest_expense(expenses):
    if not expenses:
        return None

    lowest = expenses[0]

    for expense in expenses:
        if expense.amount < lowest.amount:
            lowest = expense

    return lowest


def category_wise_expense(expenses):
    categories = {}

    for expense in expenses:
        category = expense.category

        if category not in categories:
            categories[category] = 0

        categories[category] += expense.amount

    return categories


def show_report(expenses):

    if not expenses:
        print("\nNo expenses available for report.")
        return

    print("\n========================================")
    print("          EXPENSE REPORT")
    print("========================================")

    total = total_expense(expenses)
    average = average_expense(expenses)
    highest = highest_expense(expenses)
    lowest = lowest_expense(expenses)
    categories = category_wise_expense(expenses)

    print(f"\nTotal Spending: ₹{total:.2f}")
    print(f"Average Spending: ₹{average:.2f}")

    print("\nHighest Expense:")
    print(
        f"₹{highest.amount:.2f} - "
        f"{highest.category} - "
        f"{highest.description}"
    )

    print("\nLowest Expense:")
    print(
        f"₹{lowest.amount:.2f} - "
        f"{lowest.category} - "
        f"{lowest.description}"
    )

    print("\nCategory-wise Spending:")

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")

    print("========================================")
