invite=['Ayesha','Kainat','Anam']
print(invite[0])
print(invite[1])
print(invite[-1])
message=("\tI would like to invite you on dinner ")
print(invite[0]+message)
print(invite[-2]+message)
print(invite[2]+message)
message1=(invite[0]+"can't attend the dinner")
print(message1)
invite[0]='Sadia'
print(invite)
invite.insert(0,'Harram')
invite.insert(2,'Nimra')
invite.append('aqsa')
print(invite)