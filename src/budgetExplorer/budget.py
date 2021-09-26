import math

from budgetExplorer.budget_chart_helpers import (
    extract_categories_withdrawl_data,
    generate_chart,
    get_categories_withdrawls_percentages,
)


class Category:
    def __init__(self, category_name):
        self.category_name = category_name

        self.ledger = []

    def get_balance(self):
        return sum(i["amount"] for i in self.ledger)

    def check_funds(self, amount):
        balance = self.get_balance()
        return balance >= amount

    def deposit(self, amount, des=""):
        self.ledger.append({"amount": amount, "description": des})

    def withdraw(self, amount, des=""):
        balance = self.get_balance()

        if balance >= amount:
            self.deposit(-amount, des)
            return True
        else:
            return False

    def transfer(self, amount, category_obj):
        balance = self.get_balance()

        if balance >= amount:
            self.withdraw(amount, f"Transfer to {category_obj.category_name}")
            category_obj.deposit(amount, f"Transfer from {self.category_name}")
            return True
        else:
            return False

    def __str__(self):
        max_column_length = 30
        str_output = ""

        # Adding heading text.
        str_output += self.category_name.center(max_column_length, "*")
        str_output += "\n"

        # Adding each item in ledger as new column.
        for item in self.ledger:
            # Getting first 23 characters of description.
            description = item["description"][:23]
            # Getting first 7 characters (maximum) of amount, with decimal formatting's.
            amount = item["amount"]
            amount_with_decimal = f"{float(amount):.2f}"[:7]

            # Getting padding details. (Spaces between "description" and "amount")
            padding_length = max_column_length - (
                len(description) + len(amount_with_decimal)
            )
            padding_string = padding_length * " "

            str_output += (
                description + padding_string + amount_with_decimal + "\n"
            )

        str_output += f"Total: {self.get_balance():.2f}"

        return str_output


def create_spend_chart(categories):
    categories_with_withdrawls_data = extract_categories_withdrawl_data(
        categories
    )

    categories_withdrawl_percentages = get_categories_withdrawls_percentages(
        categories_with_withdrawls_data
    )

    return generate_chart(categories_withdrawl_percentages)
