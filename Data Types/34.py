# Write a Python script to merge two Python dictionaries.

d1 = {'name': 'James', 'age': 20}
d2 = {'gender': 'male', 'country': 'Nepal'}

dict = {}
for d in [d1, d2]:
    dict.update(d)

print(dict)
