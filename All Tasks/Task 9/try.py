print("Give two numbers and divide them")
print("Enter q too quit")
while True:
    first_number=input("\n First Number:")
    if first_number=='q':
        break
    second_number=input("\n second Number:")
    if second_number=='q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't divide by 0!")
    else:
        print(answer)