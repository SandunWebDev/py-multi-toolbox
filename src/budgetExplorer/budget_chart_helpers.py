"""Here we have defined multiple helper functions directly used by "budgetExplorer.budget" 's chart related functions."""


def extract_categories_withdrawl_data(category_list):
    categories_with_withdrawls_data = {}

    for category in category_list:
        ledger_with_only_withdrawls_entries = filter(
            lambda x: x["amount"] <= 0, category.ledger
        )

        # Each withdrawl amount as positive number.
        withdrawl_amount_list = map(
            lambda x: abs(x["amount"]), ledger_with_only_withdrawls_entries
        )

        withdrawl_amount_sum = sum(withdrawl_amount_list)

        # Outting data in format of { CATEGORY NAME : { CATEGORYDATA }}
        categories_with_withdrawls_data[category.category_name] = {
            "entries": ledger_with_only_withdrawls_entries,
            "amountList": list(withdrawl_amount_list),
            "sum": withdrawl_amount_sum,
        }

    return categories_with_withdrawls_data


def get_categories_withdrawls_percentages(categories_with_withdrawls_data):

    # Calculating total sum of withdrawal amounts in all provided categories.
    total_withdrawl_sum = sum(
        category_data["sum"]
        for category_data in categories_with_withdrawls_data.values()
    )

    # Will contain tuple for each category in format of (CATEGORY_NAME, PERCENTAGE)
    categories_withdrawl_percentages = []

    for category_dict in categories_with_withdrawls_data.items():
        category_name, category_data = category_dict
        percentage = (category_data["sum"] / total_withdrawl_sum) * 100

        # Rounding down to nearest 10.
        rounded_percentage = int(percentage / 10) * 10

        categories_withdrawl_percentages.append(
            (category_name, rounded_percentage)
        )

    return categories_withdrawl_percentages


def generate_chart(categories_withdrawl_percentages):  # noqa: WPS231
    """
    Example:.

    100|
    90|
    80|
    70|
    60| o
    50| o
    40| o
    30| o
    20| o  o
    10| o  o  o
    0| o  o  o
        ---------
        F  C  A
        o  l  u
        o  o  t
        d  t  o
            h
            i
            n
            g
    """

    def generate_chart_bar_area(categories_withdrawl_percentages):

        chart_area_string = ""

        chart_area_string += "Percentage spent by category\n"  # Adding Title.

        # Adding Chart Bars. (Chart data throughout 0 - 100 in y axis)
        for chart_column_val in range(100, -10, -10):
            column_string = ""

            # Each column's prefix.
            column_string += str(chart_column_val).rjust(3) + "| "

            # Representing each columns data for each category.
            for _, percentage in categories_withdrawl_percentages:
                if percentage >= chart_column_val:
                    column_string += "o  "

            chart_area_string += column_string + "\n"

        return chart_area_string

    def generate_chart_legend_area(categories_withdrawl_percentages):
        chart_area_string = ""

        # Adding Chart legends seperator line.
        # (For. match with "xxx|" in chart bar area. Ex. 100|)
        left_padding = " " * 4
        legend_seperator_line = (
            left_padding + len(categories_withdrawl_percentages) * "---" + "\n"
        )
        chart_area_string += legend_seperator_line

        # Maximum legend name length.
        max_category_name_len = max(
            [len(x[0]) for x in categories_withdrawl_percentages]
        )

        # Genrating each column_names top to bottom. (One character per column per legend)
        for legend_column_index in range(max_category_name_len):
            column_string = ""
            column_string += left_padding + " "
            is_first_line = legend_column_index == 0

            for category_name, _ in categories_withdrawl_percentages:
                is_letter_exist = legend_column_index < len(category_name)

                if is_letter_exist:
                    character = category_name[legend_column_index]
                    formatted_character = (
                        character.upper()
                        if is_first_line
                        else character.lower()
                    )

                    column_string += f"{formatted_character}  "
                else:
                    column_string += "   "

            column_string += "\n"
            chart_area_string += column_string

        return chart_area_string

    return generate_chart_bar_area(
        categories_withdrawl_percentages
    ) + generate_chart_legend_area(categories_withdrawl_percentages)
