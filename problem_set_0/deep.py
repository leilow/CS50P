# a program that ask for the answer to life
# the answer is always 42

answer = str(input("What's the answer the life's greatest questions? "))

acceptedVars = ["42", "forty-two", "forty two"]
if answer in acceptedVars:
    print("Yes")
else:
    print("No")