# loop control statements: change a loops execution from its normal sequence

# break: used to terminate the loop entirely
# continue: skips to the iteration of the loop
# pass: does nothing, acts as a placeholder

i = 1
n = 5

# break
while i <= n:
    print(i)
    i = i + 1
    if i == 4:
        break

# continue
current_level = 0
final_level = 5

game_completed = True

while current_level <= final_level:
    if game_completed:
        current_level += 1
        if current_level == 3:  # skips level 3
            continue
        print('You have passed level', current_level)

print('Level Ends')

# pass
for index in range(1,21):
    if index == 10:
        pass
    else:
        print(index)