# .................rollercoster challenge.................
# print("Welcome to rollercoster")
# height = int(input("your height\n"))
# price = 0
# if height >= 120:
#     print("you can ride rollercoster")
#     new_age = int(input("your new age\n"))
#     if new_age < 12:
#         price += 5
#         print("please pay $5")
#     elif new_age <= 18:
#         price += 7
#         print("please pay $7")
#     else:
#         price += 12
#         print("please pay $12")

#     photos = input("do you want a photo taken? yes or no\n")
#     if photos == "yes":
#         print("please pay $3 extra")
#         # picture_price = 3
#         # total_price = picture_price + price
#         # print(f"your total bill is ${total_price}")
#         price += 3
#         print(f"your total bill is ${price}")
#     else:
#         print(f"your total bill is ${price}")
# else:
#     print("sorry, you can't ride rollercoster")


# ............pizza order challenge..............
"""
    small pizza: $15
    medium pizza: $20
    large pizza: $25
    
    pepperoni for small pizza: +$2
    pepperoni for medium or large pizza: +$3
    
    extra cheese for any size pizza: +$1
"""
# print("Welcome to Pizza Deliveries")
# size = input("What size pizza do you want? S, M or L\n")
# add_pepperoni = input("do you want pepperoni? Y OR N\n")
# extra_cheese = input("do you want extra cheese? Y OR N\n")
# pizza_price = 0

# if size == "S":
#     pizza_price += 15
#     print(f"Small Pizza Price is ${pizza_price}")
# elif size == "M":
#     pizza_price += 20
#     print(f"Small Pizza Price is ${pizza_price}")
# else:
#     pizza_price += 25
#     print(f"Small Pizza Price is ${pizza_price}")

# if add_pepperoni == "Y":
#     if size == "S":
#         pizza_price += 2
#         print("you have to pay extra $2 for pepperoni")
#     else:
#         pizza_price += 3
#         print("you have to pay extra $3 for pepperoni")
# if extra_cheese == "Y":
#     pizza_price += 1
# print(f"your final bill is ${pizza_price}")


# ............love calculator..............
print("Welcome yo Love Calculator 💖")
your_name = input("WHAT IS YOUR NAME: ")
their_name = input("WHAT IS THEIR NAME: ")

combined_name = your_name + their_name
lower_case_string = combined_name.lower()  # lower:convert to lowercase

# count:Returns the number of times a specified value occurs in a string
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

print(love_score)

if love_score < 10 or love_score > 90:
    print(
        f"Your love score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together")
else:
    print(f"your score is {love_score}, oh gosh true love still exists")
