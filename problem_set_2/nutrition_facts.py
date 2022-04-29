# input a fruit (case sensitive)
# output number of calories in one porition of fruit
# assume users input fruits exactly as written
# ignore input that is not fruit

fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
}

item = input("Item: ").lower()

for key in fruits:
    if key in item:
        print("Calories: ", fruits[key])