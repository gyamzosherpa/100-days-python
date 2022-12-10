# ----------------------------day-9:dictionary------------------------------
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
    # 123: "number datatype"
}
print(programming_dictionary)

# retrieving items from dictionary
print(programming_dictionary["Function"])
# print(programming_dictionary[123])

# adding new items to dictionary
programming_dictionary["loop"] = "The action of doing something over and over again"
print(programming_dictionary)

# create an empty dictionary
# empty_dictionary = {}
# empty_dictionary["a"] = "Features"
# print(empty_dictionary)

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# edit an item in a dictionary
# programming_dictionary["Bug"] = "Hello"
# print(programming_dictionary["Bug"])  # change definition of Bug

# loop through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# --------nesting a List in Dictionary----------

# Nesting a Dictionary in Dictionary
travel_log = {
    "Nepal": {"cities_visited": ["Pokhara", "Dharan", "Illam", "Kathmandu"]},
    "Germany": {"cities_visited":["Berlin", "Munchen", "Dortmund"]}
}
print((travel_log))

# Nesting Dictionary in a List
travel_log_update = [
    {
        "country": "Nepal",
        "cities_visited": ["Pokhara", "Dharan", "Illam", "Kathmandu"],
        "total_visits":12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Munchen", "Dortmund"],
        "total_visits":5
    },
]

print(travel_log_update)