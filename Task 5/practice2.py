required_toppings=['peproni','mashroom','olive']
for required_topping in required_toppings:
    if required_topping=='olive':
        print("Sorry olives are out of stock")
    else:
        print("Adding extra "+required_topping)  
print('enjoy your pizza')     