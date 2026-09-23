from datetime import datetime


def validate_amount(amount):
    try:
        amount = float(amount)

        if amount <= 0:
            return False, "Amount must be greater than 0."

        return True, amount

    except ValueError:
        return False, "Please enter a valid number."


def validate_date(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True, date

    except ValueError:
        return False, "Date must be in DD-MM-YYYY format."


def validate_category(category):
    if not category.strip():
        return False, "Category cannot be empty."

    return True, category.strip()


def validate_description(description):
    if not description.strip():
        return False, "Description cannot be empty."

    return True, description.strip()
