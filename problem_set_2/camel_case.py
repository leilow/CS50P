# mixed case = preferredFirstName
# snack casee = preferred_first_name

# create program that inputs camel case, outputs snake case

camelCase = input("camelCase: ")
print("snake_case: ", end="")

for letter in camelCase:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")

print()