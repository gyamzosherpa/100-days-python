# ...............................day-1......................................

# print function
print("Day-1 : Python Print Function")
print('print("what to print")')

# ........string manipulation.........
# \n : print in newline
print("hello world!\nHello world!")

# string concatenation
# " " : space
print("Hello" + " " + "Gyamzo")

# input function: ask for user input
input("What is your name?\n")
print("Hello" + " " + input("What is your last name\n"))

# len : total character
print(len(input("What is your name?\n")))

# variable
name = input("how u doing?\n")
print(name)

address = "north london"
address = "east london"
print(address)  # east london

fullName = input("what is ur fullName?\n")
length = len(fullName)
print("total character:", length)

# write a program that switches the values stored in the variables a and b
a = input("a:")
b = input("b:")

# c = a
# a = b
# b = c

a, b = b, a
print('value of a:', a)
print('value of b:', b)

"""
    ............variable naming rules.............:
    -A variable name must start with a letter or the underscore character
    -A variable name cannot start with a number
    -A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    -Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
