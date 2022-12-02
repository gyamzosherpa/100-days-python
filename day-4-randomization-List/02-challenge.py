# ------------virtual coin toss program-----------
# 1 means Heads, 0 means tails.

import random

coin_toss = random.randint(0, 1)
first_side = "heads"
second_side = "tails"

if coin_toss == 1:
    print(first_side.capitalize())
else:
    print(second_side.capitalize())
