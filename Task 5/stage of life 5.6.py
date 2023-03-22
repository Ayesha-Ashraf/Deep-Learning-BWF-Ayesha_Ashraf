age= 27
if age < 2:
    person='baby'
elif (age > 2) & (age<4):
    person='toddler'
elif (age > 4) & (age<13):
    person='kid'
elif (age > 13) & (age<20):
    person='teenager'
elif (age > 20) & (age<65):
    person='adult'
elif (age > 65) :
    person='older'
print('person  age is '+ str(person))