# ------------------day-5-----------------------
# loop: allows same line of code to execute multiple times
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
