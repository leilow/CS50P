# a program that lets the user do math
# hint: x, y, z = expression.split(" ")

expression = input("Tell me a math expression: ")
num = eval(expression)
print(float(num))