# set: collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife", "knife"}
dishes = {"bowl", "plate", "cup"}

utensils.add("napkin")
utensils.update(dishes)

for x in utensils:
    print(x)