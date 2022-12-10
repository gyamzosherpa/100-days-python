# ----------------------------day-8------------------------------
# def greet():
#     print("hello")
#     print("how do you do?")
#     print("isn't the weather nice today?")
#
#
# greet()


# ------function with inputs--------
# def my_function(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# my_function('Gyamzo')


# -------positional vs keyword Arguments-------
# function with more than 1 input
def greet_value(name, age, address):
    print(f"I'm {name}, i m {age} years old and i'm from {address}")

# function with positional argument
greet_value("Gyamzo", 26, "Swayambhu")


def greet_with(name, location):
    print(f"I'm {name}, and i'm from {location}")

# function with keyword arguments
greet_with(location = "Kathmandu", name = "Gyamzo", )