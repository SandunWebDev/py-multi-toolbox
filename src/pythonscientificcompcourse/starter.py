from arithmeticArranger import arrange_arithmetics


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


def main():
    arrange_arithmetics_runner()


if __name__ == "__main__":
    main()
