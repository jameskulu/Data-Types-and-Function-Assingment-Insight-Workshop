# 40. Write a Python program to add an item in a tuple

tup = (3, 4, 5, 6, 2, 43, 12)

lst_tup = list(tup)  # Conveting in list
new_data = [1, 3]
lst_tup.extend(new_data)  # addning an item
new_tuple = tuple(lst_tup)  # converting in tuple
print(new_tuple)
