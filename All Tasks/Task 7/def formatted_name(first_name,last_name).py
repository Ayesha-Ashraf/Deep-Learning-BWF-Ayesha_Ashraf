def get_formatted_name(first_name,last_name):
    """ Return a full name"""
    full_name=first_name+''+ last_name
    return full_name.title()
    
while True:
     print('\n tell your name')
     f_name=input("first name:")
     l_name=input("Last name:")
     formatted_name=get_formatted_name(f_name , l_name)
     print("\n hi,"+  formatted_name +"!")