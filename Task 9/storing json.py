import json 
def get_stored_username():
    """get stored username"""
    filename='username.json'
try:
    with open(filename) as f_obj:
        username=json.load(f_obj)
except FileNotFoundError():
    return None
else:
    return username
def get_new_username():
    """Prompt for a new username"""
    username=input("what is your name?")
    filename='username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        return username
def greet_user():
    """Greet the user name"""
    username=get_stored_username()
    if username:
        print("Welcome Back ,"+ username +"!")
    else:
        username=input("What is your name?")
        filename='username.json'
        with open(file,'w')as f_obj:
            json.dump(username,f_obj)
            print("we ll remember you when you come back,"+ username +"!")
greet_user()

    