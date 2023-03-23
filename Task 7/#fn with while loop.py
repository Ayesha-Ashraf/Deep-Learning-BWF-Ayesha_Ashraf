#fn with while loop
def get_formatted_name(first_name,last_name):
    """ Return a full name"""
    full_name=first_name+''+ last_name
    return full_name.title()
    
while True:
     print('\n tell your name')
     print("(Enter 'q' at any time to quit)")
     f_name=input("first name:")
     if f_name=='q':
        break
     l_name=input("Last name:")
     if l_name=='q':
        break
     formatted_name=get_formatted_name(f_name , l_name)
     print("\n hi,"+  formatted_name +"!")