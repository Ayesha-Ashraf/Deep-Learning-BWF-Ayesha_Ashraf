import time

# get the start time
st = time.time()

users=['Ali','farhan','amna','admin']
for user in users:
    if user=='admin':
        print('would like to see the status report')
    else:
        print("Hi" +user+ "thanks for login")    
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')