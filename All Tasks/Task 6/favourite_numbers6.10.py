favourite_numbers={
'Ayesha':[1,2],
'Aqsa':[7,56],
'Abdul Aziz': [26],
}
for name, numbers in favourite_numbers.items():
    print("\n",name.title()+"'s  favourite numbers are :") 
    for number in numbers:
        print("\t"+str(number))
