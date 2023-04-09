from pizza import make_pizza
pizza.make_pizza('pepperoni')
pizza.make_pizza('chesse','mushroom','olives')
#as alias
from pizza import make_pizza as mp
mp.make_pizza('pepperoni')
mp.make_pizza('chesse','mushroom','olives')
#import all function
from pizza import *
make_pizza('pepperoni')
make_pizza('chesse','mushroom','olives')