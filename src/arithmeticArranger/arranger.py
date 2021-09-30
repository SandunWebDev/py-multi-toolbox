from arithmeticArranger.arranger_helpers import (
    arrange_multiple_calc_strings,
    calculate_operands_by_type,
    find_operands,
    find_operator,
    get_arrangement_data_of_calc_string,
)


def arrange_arithmetics(calc_string_list=None, should_calculate=False):
    """Arrange Arithmetics.

    Arrange given “Arithmetic Strings” into specific formatted way.

    Args:
        calc_string_list (list): List containing each arithmetic strings.
        should_calculate (bool): Should display calculation result or not.

    Returns:
        str: Single string, formatted line by line.

    """

    # Track arranged data details for each calc_string.
    arranged_calc_data_list = []

    # Base requirements & error handling.
    if calc_string_list is None:
        return "Error: Problems not provided."
    elif len(calc_string_list) > 5:
        return "Error: Too many problems."

    # Getting arrangement data for each calc_string. (Like operator, operands, column_size, ...)
    for calc_string in calc_string_list:
        # Removing all whitespaces.
        formatted_calc_string = calc_string.replace(" ", "")

        try:
            operator_type, operator_location = find_operator(
                formatted_calc_string
            )

            operands = find_operands(formatted_calc_string, operator_type)

            arrangement_data_of_calc = get_arrangement_data_of_calc_string(
                operator_type, operands, should_calculate
            )

            arranged_calc_data_list.append(arrangement_data_of_calc)
        except Exception as err:
            return str(err)

    # Representing all calc_string in single linear fashion.
    # Ex. ["10 + 20", "100 - 50"] ---->
    #
    #     10      100
    #   + 20    -  50
    #   ----    -----
    return arrange_multiple_calc_strings(arranged_calc_data_list)
