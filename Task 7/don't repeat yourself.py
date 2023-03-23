#don't repeat your code
def sub_calc(sub_num, total_num, obtain_num):
    """Calculate BMI from weight in kg and height in meters"""
    sub = int((obtain_num*100) /total_num )
    subject = 'subject' + str(sub_num)
    print("sub {} = {}".format(subject, sub))

# Subject data = [weight_kg, height_m]
subjects =[[1, 80, 100], # subject1
           [2, 69, 75], # subject2
           [3, 80, 100], # subject3
           [4, 80, 100], # subject4
           [5, 72, 75]] # subject5

for sub in subjects:
    sub_calc(sub[0], sub[1], sub[2]) 

