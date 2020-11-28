# 15. Write a Python program to filter a list of integers using Lambda.

lst = [4, 6, 7, 5, 2, 40, 50, 38, 12]
filtered_list = list(filter(lambda x: x > 10, lst)
                     )  # Filtering greater than 10
print(filtered_list)
