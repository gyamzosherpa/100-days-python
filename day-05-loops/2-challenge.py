# 1.----------------average height challenge-----------------

# student_heights = input("Input a list of student heights\n").split()

# # range(): (a,b,c), a=start_point,b=end_point,c=increase/decrease
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     # print(student_heights[n])
# print("list of students height:", student_heights)

# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print("total students:", number_of_students)

# total_height = 0
# for height in student_heights:
#     total_height += height
# print("students total height:", total_height)

# average_height = round(total_height/number_of_students, 2)
# print("student average height:", average_height)

# -----------------challenge-2: highest score------------------
# student_scores = input("Input a list of student scores\n").split()

# for n in range(0, len(student_scores)):
#     student_scores[n] = int((student_scores[n]))
# print(student_scores)

# # print(max(student_scores)) # max(): max value

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"the highest score in the class is {highest_score}")

# -------------challenge-3: adding even number------------------
# numbers = input("Input a list of numbers\n").split()
# for n in range(0, len(numbers)):
#     numbers[n] = int(numbers[n])
# print(numbers)

# add_even_numbers = 0

# for even in numbers:
#     if even % 2 == 0:
#         add_even_numbers += even
# print(f"sum of even numbers: {add_even_numbers}")

# # using range() function
# total = 0
# for even_num in range(2, 101, 2):
#     total += even_num
# print(total)

# -------------Python program to print even Numbers in a List-------
# # list of numbers
# list1 = [10, 21, 4, 45, 66, 93]

# # using list comprehension
# even_nos = [num for num in list1 if num % 2 == 0]
# print("Even numbers in the list: ", even_nos)

# --------------challenge-4: fizz buzz------------------------
"""
    divisible by 3 = "Fizz"
    divisible by 5 = "Buzz"
    divisible by both 3 and 5 = "FizzBuzz"
"""
for new_num in range(1, 101):
    if new_num % 3 == 0 and new_num % 5 == 0:
        print("FizzBuzz")
    elif new_num % 3 == 0:
        print("Fizz")
    elif new_num % 5 == 0:
        print("Buzz")
    else:
        print(new_num)
