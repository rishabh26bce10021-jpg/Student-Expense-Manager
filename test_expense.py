import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from expense import Expense
from validation import (
    validate_amount,
    validate_date,
    validate_category,
    validate_description
)


def test_expense_creation():
    expense = Expense(
        1,
        "22-09-2026",
        150,
        "Food",
        "Lunch"
    )

    assert expense.expense_id == 1
    assert expense.date == "22-09-2026"
    assert expense.amount == 150
    assert expense.category == "Food"
    assert expense.description == "Lunch"


def test_valid_amount():
    valid, result = validate_amount("150")

    assert valid is True
    assert result == 150


def test_invalid_amount():
    valid, result = validate_amount("-50")

    assert valid is False


def test_valid_date():
    valid, result = validate_date("22-09-2026")

    assert valid is True


def test_invalid_date():
    valid, result = validate_date("2026-09-22")

    assert valid is False


def test_valid_category():
    valid, result = validate_category("Food")

    assert valid is True
    assert result == "Food"


def test_empty_category():
    valid, result = validate_category("")

    assert valid is False


def test_valid_description():
    valid, result = validate_description("Lunch")

    assert valid is True
    assert result == "Lunch"


def test_empty_description():
    valid, result = validate_description("")

    assert valid is False





