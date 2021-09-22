OPERATIONS = ["+", "-"]  # Operations allowed in "calc_strings"

"""
    Here we have defined multiple helper functions directly used by "arithmeticArranger.arranger.arrange_arithmetics()" function.

    SIDENOTE :
        - "calc_strings" represent, linear representation of arithmetic calculation. (Ex. "100 + 25")
"""


def find_operator(calc_string):
    operator_location = None
    operator_type = None

    for operator in OPERATIONS:
        operator_location = calc_string.find(operator)

        if operator_location > -1:
            operator_type = operator
            break

    if operator_location == -1:
        raise Exception("Error: Operator must be '+' or '-'.")

    return (operator_type, operator_location)


def find_operands(calc_string, operator_type):
    operands = calc_string.split(operator_type)
    operands_as_numerical = []

    try:
        operands_as_numerical = list(map(int, operands))
    except Exception as err:
        raise Exception("Error: Numbers must only contain digits.") from err

    for operand in operands:
        if len(str(operand)) > 4:
            raise Exception("Error: Numbers cannot be more than four digits.")

    return operands_as_numerical


def calculate_operands_by_type(operator_type, operands):
    operand1, operand2 = operands
    numeric_ans = 0

    if operator_type == "+":
        numeric_ans = operand1 + operand2
    elif operator_type == "-":
        numeric_ans = operand1 - operand2

    return numeric_ans


def get_arrangement_data_of_calc_string(
    operator_type, operands, should_calculate=False
):

    operand1, operand2 = operands
    largest_length_operand = max(operands, key=lambda x: len(str(x)))
    max_operand_len = len(str(largest_length_operand))
    # Length, each column should be. (Including operator_type + whitespace + operand )
    column_length = (
        max_operand_len + 2  # Addition "2" is for "operator_type + whitespace"
    )

    columns_list = [
        # First Column.
        str(operand1).rjust(column_length),
        # Second Column.
        operator_type + " " + str(operand2).rjust(column_length - 2),
        # Third Column.
        "-" * column_length,
    ]

    if should_calculate:
        fourth_column_data = calculate_operands_by_type(operator_type, operands)
        fourth_column = str(fourth_column_data).rjust(column_length)

        columns_list.append(fourth_column)

    return (
        columns_list,
        column_length,
    )


def arrange_multiple_calc_strings(arranged_calc_data_list, spaces=4):

    combind_columns = []

    for calc_index, arranged_calc_data in enumerate(arranged_calc_data_list):
        column_list, column_length = arranged_calc_data
        deafult_seperator_spaces = " " * spaces

        for index, column_text in enumerate(column_list):
            seperator_spaces = deafult_seperator_spaces

            if calc_index == len(arranged_calc_data_list) - 1:
                seperator_spaces = ""

            try:
                combind_columns[index].append(column_text + seperator_spaces)
            except IndexError:
                combind_columns.append([column_text + seperator_spaces])

    flattened_columns = list(map(lambda x: "".join(x), combind_columns))

    return "\n".join(flattened_columns)
