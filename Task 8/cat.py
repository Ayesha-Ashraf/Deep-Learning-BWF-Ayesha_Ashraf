class Cat():
    """A simple aattempt to model cat"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
         """Stimulate a cat sitting in response command"""
         print(self.name.title()+"is nowsitting ")
    def roll_over(self):
        """Stimulate a cat sitting in response command"""
        print(self.name.title()+"is roll over ")  
class Cat():
    my_cat= Cat('koko',4)
    print("my cat name is "+my_cat.name.title()+".")
    print("my cat name is "+str(my_cat.age)+".")                   

     