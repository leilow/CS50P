# a program that tells you what time to eat
# 24 hour clock, #:## or ##:##

# breakfast 7-8am (1 hour)
# lunch 12-13pm (1 hour)
# dinner 18-19pm (1 hour)
# not meal time, no output

# hint: hours, minutes = time.split(":")

def main():
    """
    get time from user
    call convert function
    breakfast, lunch, dinner times
    """
    time = input("What time is it? Please use 00:00 formatting: ")
    c_time = convert(time)
    # print(c_time)
    meal_time(c_time)

def convert(time):
    """
    get hour minute
    convert time into float
    return result to main function
    """
    hours, minutes = time.split(":")
    c_hours = int(hours)
    c_minutes = int(minutes)
    c_time = c_hours + c_minutes/60
    # print(f"{c_time:.2f}")
    return c_time

def meal_time(c_time):
    if c_time >= 7 and c_time <= 8:
        print("It's breakfast time.")
    elif c_time >= 12 and c_time <= 13:
        print("It's lunch time.")
    elif c_time >= 18 and c_time <= 19:
        print("It's dinner time.")
    else:
        print("No meals at this time.")

if __name__ == "__main__":
    main()