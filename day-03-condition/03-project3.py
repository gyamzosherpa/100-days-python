# ..............project 3.............
# https://ascii.co.uk/oneline
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure island.")
print("Your mission is to find the treasure.")

choice1 = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()

if choice1 == 'left':
    # continue in the game
    swim_walk = input("Do you want to swim or wait\n").lower()
    if swim_walk == "wait" or "Wait" or "WAIT":
        # game will continue
        door = input("which door? red, blue or yellow\n").lower()
        if door == "red":
            print("game over")
        elif door == "blue":
            print("game over")
        else:
            print("You win")
            print('''  _                           
    | |                          
  __| | __ _ _ __   ___ ___  ___ 
 / _` |/ _` | '_ \ / __/ _ \/ _ \
| (_| | (_| | | | | (_|  __/  __/
 \__,_|\__,_|_| |_|\___\___|\___|''')
    else:
        print("Game over")
else:
    print("Game over")
