# -------------------------day-4-------------------------------

import string  # random string
import random  # random number
import my_module  # your random file

# # generate random number: randomInt takes two arguments
# random_int = random.randint(1, 10)  # 1 to 10
# print(random_int)

# # generating random alphabet (aA-zZ)
# all_alphabets = string.ascii_letters.lower()
# result = random.choice(all_alphabets)
# print(result)

# print(round(my_module.pi, 2))

# # generating random floating point numbers: 0.000 to 0.9999
# random_float = round(random.random() * 5, 2)
# print(random_float)

# lists: ["gyamzo","london","ozil"]
# parties_of_nepal = ["UML", "Maoist", "Congress", "RSP", "RPP"]
# print(parties_of_nepal)
# print(parties_of_nepal[4])

# parties_of_nepal[1] = 'RSP'  # modify second list
# print(parties_of_nepal)

# parties_of_nepal.append("My-party")  # append: add new list to last
# print(parties_of_nepal)

# parties_of_nepal.extend("hell")  # 'h','e','l','l'
# print(parties_of_nepal)

# parties_of_nepal.extend(["naya-party","purano-party"])  # add two new list at last
# print(parties_of_nepal)

# parties_of_nepal.insert(0, "new_party")  # Insert an item at a given position
# print(parties_of_nepal)

# # pop(1): remove 2nd item, if no position given, last element deleted
# parties_of_nepal.pop(1)
# print(parties_of_nepal)

# # remove:first element removed
# # list.clear():Remove all items from the list.

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits.count('apple')) # 2 bananas

# print(fruits.index('banana'))  # start at 3 position
# print(fruits.index('banana', 4))  # Find next banana starting at position 4

# fruits.sort()  # ascending order
# print(fruits)

# list methods: https://docs.python.org/3/tutorial/datastructures.html

# index errors and nested lists

nepal_states = ["pradesh1", "Madhesh Province",
                "Bagmati Province", "Lumbini Province", "Karnali Province", "Sudurpashchim Province"]
no_of_states = len(nepal_states)
print(nepal_states[no_of_states - 1])

fruits = ["mango", "grapes", "apple", "banana"]
vegetables = ["tomato", "potatoes", "spinach"]

fruits.append(vegetables)
print(fruits)

# fruits_vegetables = [fruits, vegetables]  # two list combine
# print(fruits_vegetables)
