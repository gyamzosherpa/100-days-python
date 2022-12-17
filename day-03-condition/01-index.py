# ..........................day-3....................................
# ....... condition, if/else.........
# room_no = 16
# if room_no == 16:
#     print("welcome to the king room 👑")
# else:
#     print("sorry, you are in wrong room")

# ..........................
# height = int(input("what is your height in cm?\n"))

# if height >= 120:
#     print("you can ride the rollercoster.")
# else:
#     print("sorry, you have to grow taller before you can ride.")

# write a program that works out whether if a given number is an odd or even number

# number = int(input("enter number\n"))

# if number % 2 != 0:  # != (not equal to)
#     print("odd number")
# else:
#     print("even number")

# ...........if/else/elif.............
# age = int(input("your age please:\n"))
# if age == 17:
#     print("you can watch romantic movie")
# elif age >= 18:
#     print("you can watch 18+ movies")
# else:
#     print("you are not allowed to watch such movies")

# .........nested if/else/elif............ 🤣
# new_height = int(input("your new height\n"))

# if new_height >= 120:
#     print("you can ride rollercoster")
#     new_age = int(input("your new age\n"))
#     if new_age < 12:
#         print("please pay $5")
#     elif new_age <= 18:
#         print("please pay $7")
#     else:
#         print("please pay $12")
# else:
#     print("sorry, you can't ride rollercoster")

"""
    bmi 2.0, if:
    under 18.5 = underweight
    over 18.5 but below 25 = normal weight
    over 25 but below 30 = overweight
    over 30 but below 35 = obese
    above 35 = clinically obese
"""
# bmi_height = float(input("your height\n"))
# bmi_weight = float(input("your weight\n"))
# bmi = round(bmi_weight/(bmi_height ** 2), 2)

# if bmi < 18.5:
#     print(f"your bmi is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"your bmi is {bmi}, you have a normal weight")
# elif bmi < 30:
#     print(f"your bmi is {bmi}, you are overweight")
# elif bmi < 35:
#     print(f"your bmi is {bmi}, you are obese")
# else:
#     print(f"your bmi is {bmi}, you are clinically obese")

# leap year check, leap years = 366 days
# year = int(input("which year do you want to check: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is  a leap year")
# else:
#     print(f"{year} is not a leap year")


# ........logical operators..........

# logical and operator:both condition should be true for true
a = 59

if 45 <= a <= 55:
    print("between 45 and 55")
else:
    print("you are free to do anything")


# logical or operator: if at least one condition true, then its true
b = 59

if b >= 45 or b <= 55:
    print("between 45 and 55")
else:
    print("you are to do anything")

