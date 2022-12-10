# ------ challenege-1: Paint area calculator ------
import math

# print("------------Challenge-1------------")
# test_h = float(input("Height of the wall: "))
# test_w = float(input("Width of the wall: "))
# coverage = 5
#
# def paint_calc(height, width, cover):
#     area = height * width
#     # number_of_cans = round(area / cover)
#     number_of_cans = math.ceil(area / cover)
#     print(f"You'll need {number_of_cans} cans of paint")
#
# paint_calc(cover = coverage, height = test_h, width = test_w)

# math functions: https://docs.python.org/3/library/math.html

# ---------challenge-2: prime number checker-----------
# print("------------Challenge-2------------")
# n = int(input("Check this number: "))
#
# def prime_checker(number):
#     is_Prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_Prime = False
#     if is_Prime:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")
#
# prime_checker(number = n)

# --------challenge-3: factorial----------------
print("------------Challenge-3------------")
x = int(input("Enter the number: "))

def factorial(number):
    factorial = 1
    if number < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif number == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range (1, number + 1):
            factorial = factorial * i
            # print(factorial)
        print("The factorial of", number, "is", factorial)


factorial(number = x)


# ---------------factorial using recursion--------------
print("------------factorial using recursion------------")
def factorial_second(x):
    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial_second(x-1))

num = int(input("Enter a number: "))

# call the factorial function
result = factorial_second(num)
print("The factorial of", num, "is", result)

#------------------using math-modules---------------
print("------------factorial math module------------")
new_num = int(input("Enter a number: "))
print(math.factorial(new_num))