# 1. Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


string = input('Enter any string: ')
dict = {}

for i in string:
    dict[i] = string.count(i)

print(dict)
