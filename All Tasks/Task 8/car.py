class Car():
    """A simple attempt to represent car"""
    def __init__(self, make,model,year):
        """initialize attributes to describe car"""
        self.make=make
        self.model=model
        self.year=year
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name=str(self.year)+" "+self.make+" " +self.model
        return long_name.title()
my_new_car=Car('audi','a4','2015')
print(my_new_car.get_descriptive_name())