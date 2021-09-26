from arithmeticArranger import arrange_arithmetics
from budgetExplorer.budget import Category as BudgetCategory
from budgetExplorer.budget import create_spend_chart
from polygonHandler import polygon
from probabilityCalculator import probability as probability_calculator
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


def budget_explorer_runner():
    food = BudgetCategory("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")

    clothing = BudgetCategory("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)

    auto = BudgetCategory("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    chart = create_spend_chart([food, clothing, auto])

    print(food)
    print("\n", clothing)
    print("\n", chart)


def polygon_handler_runner():
    rect = polygon.Rectangle(10, 15)

    print(rect.get_area())
    rect.set_width(20)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = polygon.Square(5)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)


def probability_calculator_runner():
    probability_calculator.random.seed(95)
    hat = probability_calculator.Hat(yellow=5, red=1, green=3, blue=9, test=1)
    probability = probability_calculator.experiment(
        hat=hat,
        expected_balls={"yellow": 2, "blue": 3, "test": 1},
        num_balls_drawn=20,
        num_experiments=100,
    )
    print("Probability:", probability)


def main():
    # arrange_arithmetics_runner()
    # add_time_runner()
    # budget_explorer_runner()
    # polygon_handler_runner()
    probability_calculator_runner()


if __name__ == "__main__":
    main()
