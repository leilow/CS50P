import re

vowels = 'aeiouAEIOU'

input_tweet = input("Input: ")

for ch in input_tweet:
    if ch in vowels:
        input_tweet = input_tweet.replace(ch, "")

print(input_tweet)