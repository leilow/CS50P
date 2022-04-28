# tip calculator program

# inputs
bill_original = input("How much was the meal? ")
percent_og = input("How much do you want to tip? ")

# format inputs
bill_strip = float(bill_original.strip("$"))
percent_strip = float(percent_og.strip("%")) / 100

# calculate tip, print statement
tip = bill_strip * percent_strip
print(f"You can leave a ${tip:.2f} tip. That's {percent_og} on your {bill_original} check.")