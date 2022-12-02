# ....................day-2.......................

# String: "hello", 'hello'
print('hello'[0])  # h, first character is h, starts from 0
print("hello"[2])  # l
print("98123")  # 98123
print("11" + "22")  # 1122

# ........Data Types..........

# Integer
print(11 + 22)  # 33

# float
num = 1.234
print(num)

# boolean: True, False
isSingle = False
print(isSingle)

# type error, type checking, type conversion

num_char = len(input("what's ur name?\n"))
print(type(num_char))  # int
new_num_char = str(num_char)  # change number to string
print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))  # float

print(70 + float("100.5"))  # 170.5
print(str(70) + str(100))  # 70100

# write a program that adds the digits in a 2 digit number. e.g.if
# the input was 35, then the output should be 3 + 5 = 8
num1 = input("enter two digit number\n")
print(int(num1[0]) + int(num1[1]))

# mathematical operations
# PEMDAS: (), **, * /, + -, lR=left and right
print(3 * (3 + 3) / 3 - 3)  # 3
print(3**3)  # 27
print(round(8/3))  # 3

# calculate BMI, bmi=(weight/height**2)
height = float(input("enter your height in m\n"))
weight = float(input("enter your weight in kg\n"))
bmi = round((weight/(height**2)), 2)  # round: limit decimal
print("your bmi is", bmi)

# manipulation and f or F string
score = 3
score += 1
height = 1.7
isWinning = True

# f or F string: combine all dataTypes
print(
    F"your score is {score}, your height is {height}, you are winning is {isWinning}")

"""
    create a program using maths and f-strings that tells us how many days, weeks, months
    we have left if we live until 90 years old
"""
age = int(input("what is your current age?\n"))
years_remaining = 90 - age
days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12
print(f"you have {days} days, {weeks} weeks, and {months} months left")
