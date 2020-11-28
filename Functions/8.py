# 8. Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


def remove_duplicate(lst):
    new_lst = set(lst)
    return list(new_lst)


print(remove_duplicate([1, 2, 3, 3, 3, 3, 4, 5]))
