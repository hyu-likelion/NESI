from bwsi_grader.python.pizza_shop import grader


def cost_calculator(*pizzas, drinks=None, wings=None, coupon=None):
    sum = 0
    toppings = ["pepperoni", "mushroom", "olive", "anchovy", "ham"]
    toppings_price = [1.00, 0.50, 0.50, 2.00, 1.50]
    drinks_size = ["small", "medium", "large", "tub"]
    drinks_price = [2.00, 3.00, 3.50, 3.75]
    wings_size = [10, 20, 40, 100]
    wings_price = [5.00, 9.00, 17.50, 48.00]

    if len(pizzas) != 0:
        for pizza in pizzas:
            sum += 13.00
            for top, top_price in zip(toppings, toppings_price):
                sum += pizza.count(top) * top_price

    if drinks is not None:
        for drink, dr_price in zip(drinks_size, drinks_price):
            sum += drinks.count(drink) * dr_price

    if wings is not None:
        for wing, w_price in zip(wings_size, wings_price):
            sum += wings.count(wing) * w_price

    total = sum + sum * 0.0625

    if coupon is not None:
        discount = sum*coupon
        total -= discount

    round_total = round(total, 2)

    return round_total


grader(cost_calculator)
