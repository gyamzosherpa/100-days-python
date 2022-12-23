# tuple-set: collection which is ordered and unchangeable used to group together related data

student = ("Gyamzo", 26, "male")

print(student.count("Gyamzo"))
print(student.index("Gyamzo"))

for x in student:
    print(x)

if "Gyamzo" in student:
    print("Gyamzo is here")