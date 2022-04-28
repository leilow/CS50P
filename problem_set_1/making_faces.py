# return corresponding emoji

# this solution works, but I can't break it up into functions
# str1 = input("How are you feeling? ")

# var1 = {':)': '🙂',':(': '🙁',':/':'😐'}

# for Key,value in var1.items():
#     str1 = str1.replace(Key,value)
# print(str1)


def main():
    str = input("How are you feeling? ")
    result = convert(str)
    print(result)

def convert(str):
    str1 = str.replace(":)", "🙂")
    str2 = str1.replace(":(", "🙁")
    str3 = str2.replace(":/", "😐")
    return str3

main()