# Python String Methods
your_name = "gyAmzo"
print("Capitalize:", your_name.capitalize())
print("Casefold:", your_name.casefold())  # lowercase
print("Center:", your_name.center(12))  # move text
print("Count:", your_name.count("a"))  # count text character
print("endswith:", your_name.endswith("a"))  # true or false

txt = "H\te\tl\tl\to"  # t:tabs
print("expand tabs:", txt.expandtabs(10))  # increase tabs

# find: Searches the string for a specified value and returns the position of where it was found
print("find:", your_name.find("o"))

# The index() method finds the first occurrence of the specified value.
txt2 = "Hello, welcome to my world."
x = txt2.index("e", 5, 10)  # start point, end point
print(x)

# https://www.w3schools.com/python/python_ref_string.asp

# .........string slicing..........
# slicing: create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Gyamzo code"
# char_slice = name[2]  # a
# char_slice = name[0:2]  # gy
# char_slice = name[:2]  # gy
# char_slice = name[7:11]  # code
char_slice = name[7:]  # code
print(char_slice)

new_name = "hello world"
# edit_name = new_name[0:11:1]  # hello world,  [start:stop:step]
# edit_name = new_name[0:11:2]  # hlowrd
edit_name = new_name[::2]  # hlowrd
print(edit_name)

reverse_name = "gyamzo"
final_name = reverse_name[::-1]
print(final_name)  # ozmayg

website = "https://google.com"
website_name = slice(8, -4)  # [start:stop:step]
print(website[website_name])  # google