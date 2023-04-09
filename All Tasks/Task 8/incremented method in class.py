class Car():
    """A simple attempt to represent car"""
    def __init__(self, make,model,year):
        """initialize attributes to describe car"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=67
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name=str(self.year)+" "+self.make+" " +self.model
        return long_name.title()
    def read_odometer(self):
        """Print a statement  showing car mileage"""
        print("this is a car"+str(self.odometer_reading)+"miles on it")
    def update_odometer(self ,mileage):
        """Set the odometer reading to the given value reject the change"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cant roll bsack an odometer!")
    def incremented_odometer(self ,miles):
        self.odometer_reading +=miles
my_used_car=Car('sabru','outvalg','2018')
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(698)
my_used_car.read_odometer()
my_new_car=Car('audi','a4','2015')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(34)
my_new_car.read_odometer()