fvrt_languages={
    'jen':['python'],
    'ali':['c','ruby'],
    'edward':['python']
    }
for name ,languages in fvrt_languages.items():
    print("\n" + name.title()+ "'s favourite languages are :")
    for language in languages:
        print("\t"+language.title())  