# 43. Write a Python program to remove an item from a tuple.

tup = (3, 4, 5, 6, 2, 43, 12)

lst_tup = list(tup)  # Conveting in list
data_to_remove = 3
lst_tup.remove(data_to_remove)  # removing an item
new_tuple = tuple(lst_tup)  # converting in tuple
print(new_tuple)
