#modifying attribute
class Car():
    """A simple attempt to represent car"""
    def __init__(self, make,model,year):
        """initialize attributes to describe car"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=47
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name=str(self.year)+" "+self.make+" " +self.model
        return long_name.title()
    def read_odometer(self):
        """Print a statement  showing car mileage"""
        print("this is a car" + str(self.odometer_reading) + "miles on it")
my_new_car=Car('audi','a4','2015')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()