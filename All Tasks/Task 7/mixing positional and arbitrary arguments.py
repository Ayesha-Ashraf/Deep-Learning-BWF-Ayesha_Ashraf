# arbitary arguments
def make_pizza(size,*toppings):
    """Print list of pizza"""
    print("\n Making  a "+str(size)+"inch pizza with the following toppings:")
    for  topping in toppings:
        print(topping)
make_pizza(16,'pepperoni')
make_pizza(12,'chesse','mushroom','olives')