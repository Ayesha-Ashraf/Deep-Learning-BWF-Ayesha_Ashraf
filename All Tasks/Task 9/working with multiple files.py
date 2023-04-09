def count_words(filename):
    """Count the approxiamate number of words in a file"""
try:
    with open(filename) as f_obj:
        contents=f_obj.read()
except FileNotFoundError():
    msg="Sorry , the file "+filename+"does not exist"
    print(msg)
else:
    #count the approximate numbers of words
    words=contents.split()
    num_words=len(words)
    print("the file" + filename + "has about"+str(num_words)+"words.")

filenames=['digit_million.txt','pi_digits.txt','programming.txt']
for filename in filenames:
    count_words(filename)