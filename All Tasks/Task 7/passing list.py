#passing list
def greet_user(names):
    """print  simple greeting in a list"""
    for name in names:
        msg="hi,"+name.title()+"!"
        print(msg)
usernames=['hannan','ayesha','ali']
greet_user(usernames)