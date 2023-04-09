#dictionary
alien_0 = {'color':'green','points':5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
#add attribute
a = alien_0['color']
print("your colors"+str(a)+"colors!")
alien_0['direction_x']=0
print(alien_0)
#starting Empty
alien_1={}
alien_1['color']='yellow'
alien_1['points']=10
print(alien_1)
#modify
alien_0 = {'color':'green'}
print(alien_0)
alien_0 = {'color':'red'}
print(alien_0)
#remove key value
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['color']
print(alien_0)
#objects
fvrt_lang={
    'jen':'python',
    'sarah':'c',
    'ewrd':'ruby'}
print("Sarah fvrt language"+fvrt_lang['sarah'].title())
