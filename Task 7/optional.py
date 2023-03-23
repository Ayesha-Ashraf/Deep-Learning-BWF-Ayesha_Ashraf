def formatted_name(first_name, last_name, middle_name=''):
    """ Return a full name"""
    if middle_name:
         full_name= first_name +' '+ middle_name +' '+ last_name
    else:
         full_name= first_name  +' '+ last_name
    return full_name

student=formatted_name('Ayesha','Ashraf')
print(student)