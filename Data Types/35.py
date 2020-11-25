# 35. Write a Python program to iterate over dictionaries using for loops.

dict = {
    'name': 'James',
    'age': 20,
    'gender': 'male'
}

for key, items in dict.items():
    print(f'{key}:{items}')
