favourite_places ={
      'Alina' : ['murree','kalaam'] ,
      'Ayesha': ['kuwait'] ,
      'Aqsa' :['Dubai','Saudia Arabia'],
    }
for people , places  in favourite_places.items():
    print("\n",people.title()+"'s  favourite places are :")
    for place in places:
        print( "\t" + place.title())