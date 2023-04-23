# Using these lists:
list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

# Determine which items are present in both lists.
list_a_as_set = set(list_a)
intersection = list_a_as_set.intersection(list_b)
intersection_as_list = list(intersection)
print(intersection_as_list)

# Determine which items do not overlap in the lists.
new_list_a = list(set(list_a).difference(set(list_b)))
new_list_b = list(set(list_b).difference(set(list_a)))
print(new_list_a)
print(new_list_b)
new_list_a.extend(new_list_b)
print(new_list_a)