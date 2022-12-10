# -------------project-4: rock, paper and scissors---------------
"""
    Rock wins against scissors; 
    paper wins against rock; 
    and scissors wins against paper. 
    If both players throw the same hand signal, it is considered a tie, and play resumes until there is a clear winner.
"""

import random

paper = """ _ __   __ _ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |
| .__/ \__,_| .__/ \___|_|
| |         | |
|_|         |_| """

rock = """
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   <
|_|  \___/ \___|_|\_\
    """

scissors = """   ,--.
 (    )____ ___________________________
  `--'---,-'  ,.  T--------------------`-.
  ,--.---`-.  `'  |_dd____________________`>
 (    )
"""

game_images = [rock, paper, scissors]

user_choice = int(input(
    "what do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose")
else:
    print("you chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You wins")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif computer_choice < user_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("It's a draw")
