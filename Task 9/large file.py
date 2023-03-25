#string of lines
filename='digit_million.txt'
with open(filename) as file_object:
    lines= file_object.readlines()
    

digit_string= ' '
for line in lines:
    digit_string += line.rstrip()

print(digit_string[:52]+"......")
print(len(digit_string))
