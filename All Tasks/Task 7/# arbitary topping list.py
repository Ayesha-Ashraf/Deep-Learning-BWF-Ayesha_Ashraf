# arbitary arguments
def make_pizza(*toppings):
    """Print list of pizza"""
    for topping in toppings:
        print(topping)
make_pizza('pepperoni')
make_pizza('chesse','mushroom','olives')