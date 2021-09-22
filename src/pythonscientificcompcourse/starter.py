from arithmeticArranger import arrange_arithmetics
from timeCalculator import add_time


def arrange_arithmetics_runner():
    calc_string_list = []

    print("Please Enter Your String Arithmetics Below One By One : ")

    while True:
        calc_string = input("")

        if calc_string == "" or calc_string.lower() == "done":
            break
        else:
            calc_string_list.append(calc_string)

    result = arrange_arithmetics(calc_string_list)
    print(result)


def add_time_runner():
    future_date = add_time("2:59 AM", "30:00")
    print(future_date)


def main():
    # arrange_arithmetics_runner()
    add_time_runner()


if __name__ == "__main__":
    main()
