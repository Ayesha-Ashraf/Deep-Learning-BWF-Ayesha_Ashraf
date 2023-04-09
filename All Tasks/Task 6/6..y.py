languages={
    'ali':'python',
    'faizan':'c++',
    'aqsa':'ruby'
}
people=['aqsa','faizan']
for person in sorted(languages.keys()):
    print(person.title())
    if person in people:
        print(person.title() +"you have already responding")
    else:
        print(person.title()+"you havent taken pool")