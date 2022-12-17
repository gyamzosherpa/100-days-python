# -----------------------day-6---------------------
# built-in functions: https://docs.python.org/3/library/functions.html

# def my_function():
#     name = "Gyamzo"
#     print("my name is", name)
#     for n in range(1, 6, 2):
#         print(n, end=",")


# my_function()


# def multiplication():
#     num = int(input("Display multiplication table of?\n"))

#     for i in range(1, 11):
#         print(num, 'x', i, '=', num*i)


# multiplication()


# def check():
#     number = 0

#     if number > 0:
#         print("Positive number")
#     elif number == 0:
#         print('Zero')
#     else:
#         print('Negative number')


# check()

# ---------------while loop--------------------
current_level = 0
final_level = 5

game_completed = True

while current_level <= final_level:
    if game_completed:
        print('You have passed level', current_level)
        current_level += 1

print('Level Ends')
