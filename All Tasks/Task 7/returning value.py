def formatted_name(first_name,last_name):
    """ Return a full name"""
    full_name=first_name+''+ last_name
    return full_name.title()
student=formatted_name('Ayesha', 'Ashraf')
print(student)