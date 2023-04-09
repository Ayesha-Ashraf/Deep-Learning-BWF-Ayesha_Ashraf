rivers={
    'pakistan':'chanaab',
    'india':'ravi',
    'egypt':'nile'
}
for country , river in rivers.items():
    print(river.title()+" is in "+ country.title())
#2
for  river in rivers.values():
    print(river.title())
for country  in rivers.keys():
    print( country.title())
