numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number in numbers:
        position=number
    if number==1:
        position=1
    elif number==2 :
        position=2
    elif number==3 :
        position=3
    elif number==4 :
        position=4
    elif number==5 :
        position=5
    elif number==6 :
        position=6
print("the position is"+str(position)+"th")
