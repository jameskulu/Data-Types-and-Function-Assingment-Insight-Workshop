# 13. Write a Python program to sort a list of tuples using Lambda

tup = (2, 3, 5, 7, 4, 3, 5, 9, 6)

sorted_lst = sorted(tup, key=lambda x: x)
print(sorted_lst)
