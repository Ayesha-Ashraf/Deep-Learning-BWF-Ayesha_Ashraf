import json 
username=input("what is your name?")
filename='username.json'
try:
    with open(filename) as f_obj:
        username=json.load(f_obj)
except FileNotFoundError():
    username=input("what is your name?")
    with open(filename,'w') as f_obj:
         json.dump(username,f_obj)
         print("we ll remember you when you call back,"+ username +"!")
else:
    print("Welcome Back ,"+ username +"!")
