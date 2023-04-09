import json 
numbers=[2,4,6,7,8,9]
filename='number.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
