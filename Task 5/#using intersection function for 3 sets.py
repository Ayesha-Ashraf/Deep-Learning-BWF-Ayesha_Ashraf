#using intersection function for 3 sets
A={1,2,3,4}
B={3,4,8,9}
C={4,14,10,9}
print("ABC:",A.intersection(B,C))
# using symbols with "&" fo 3 sets
A={1,2,97,4}
B={4,4,0,9}
C={3,4,8,9}
print("ABC:", A&B&C)
# uing string 3 sets 
A = {'ab', 'ba', 'cd', 'dz'}
B = {'cd', 'ab', 'dd', 'za'}
C={3,4,8,9}
print("ABC:", A.intersection(B,C))
# uing string wit & 3 sets 
A = {'ab', 'ba', 'cd', 'dz'}
B = {'cd', 'swer', 'dd', 'by'}
C={3,4,99,9}

print("ABC:", A&B&C)

#empty sets
set1 = {}
set2 = {}
 
# union of two sets
set1={}
set2={}
print("set1 intersection set2 : ",
      set(set1).intersection(set(set2)))
