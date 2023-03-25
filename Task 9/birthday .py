#string of lines
filename='digit_million.txt'
with open(filename) as file_object:
    lines= file_object.readlines()
    

digit_string= ' '
for line in lines:
    digit_string += line.rstrip()

birthday=input("Enter your birthday, in the form ,mmddyy:")
if birthday in digit_string:
    print("your birthday appear in the million digits ")
else:
    print("your birthday  does not appear in the million digits ")