#returning dictionary
def build_person(first_name,last_name,age=''):
    """Return a dictionary information"""
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
student=build_person('Ayesha','Ashraf',age=22)
print(student)    
