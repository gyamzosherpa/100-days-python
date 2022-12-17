# ------------------day-5-----------------------
# loop: allows same line of code to execute multiple times
# for loop: a statement that will execute its block of code
#          : a limited amount of times
import time

fruits = ["Apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

# for loops and the range() function
# range(): (a,b,c), a=start_point,b=end_point,c=increase/decrease
# for number in range(1, 10, 2):
#     print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)  # 5050

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("happy new year")

# while loop: a statement that will execute its block of code,
#               as long as it's condition remains true
#               : unlimited

# while 1 == 1:
#     print("help me")  # continue to execute

# name = ""
# while len(name) == 0:
#     name = input("enter your name\n")
# print("hello", name)

name = ""  # name = None

while not name:
    name = input("enter your name\n")
print("hello", name)

# Python While loop with else
counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')