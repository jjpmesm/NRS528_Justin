# Using this list:
list = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]

# You need to do two separate things here and report both in your Python file. You should have two solutions in this
# file, one for item 1 and one for item 2. Item 2 is tricky so if you get stuck try your best (no penalty),
# for a hint check out the solution by desiato here.
# Make a new list that has all the elements less than 5 from this list in it and print out this new list.

new_list = []
for item in list:
    if item <5:
        new_list.append(item)
print(new_list)

# Write this in one line of Python (you do not need to append to a list just print the output).
print(*[1, 2, 3])
print([n for n in list is n < 5])