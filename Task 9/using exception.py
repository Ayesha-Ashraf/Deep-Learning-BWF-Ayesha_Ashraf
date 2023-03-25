print("Give two numbers and divide them")
print("Enter q too quit")
while True:
    first_number=input("\n First Number:")
    if first_number=='q':
        break
    second_number=input("\n second Number:")
    if second_number=='q':
        break
    answer=int(first_number)/int(second_number)
    print(answer)