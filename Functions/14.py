# 14. Write a Python program to sort a list of dictionaries using Lambda

lst = [{'name': 'Rubi', 'age': 21}, {
    'name': 'James', 'age': 20},  {'name': 'Arbin', 'age': 19}]
sorted_lst = sorted(lst, key=lambda k: k['name'])
print(sorted_lst)
