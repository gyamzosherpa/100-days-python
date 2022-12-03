# 1. ------------virtual coin toss challenge----------------
# 1 means Heads, 0 means tails.

import random

# coin_toss = random.randint(0, 1)
# first_side = "heads"
# second_side = "tails"

# if coin_toss == 1:
#     print(first_side.capitalize())
# else:
#     print(second_side.capitalize())

# 2. ---------------banker roullete challenge-----------------
# split string method
# all_names = input("Give me everybody's names, seperated by a comma. ")
# names = all_names.split(", ")

# solution-1
# get total number of items in list
# num_items = len(names)

# # generate random numbers between 0 and the last index
# random_choice = random.randint(0, num_items - 1)

# person_who_will_pay = names[random_choice]

# solution-2
# person_who_will_pay = random.choice(names)  # choice: select random elements

# print(person_who_will_pay + " is going to buy the meal today.")

# 3. --------------------treasure-map challenge------------------
row1 = ["🥲", "🥲", "🥲"]
row2 = ["🥲", "🥲", "🥲"]
row3 = ["🥲", "🥲", "🥲"]

map = [row1, row2, row3]
print(map)

print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
