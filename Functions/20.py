# 20. Write a Python program to find intersection of two given arrays using
# Lambda.

lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [4, 5, 6, 7, 8, 9]

intersection = list(filter(lambda x: x in lst1, lst2))
print(intersection)
