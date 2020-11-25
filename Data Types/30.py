# 30. Write a Python script to check whether a given key already exists in a
# dictionary.

dict = {
    'name': 'James',
    'age': 20,
    'gender': 'male'
}

key_check = 'name'

if key_check in dict.keys():
    print("Key already exists.")
else:
    print("Key does not exists.")
