# 4. Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.
# Sample String: 'abc', 'xyz'
# Expected Result: 'xyc abz'

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

first_of_string1, first_of_string2 = string2[0], string1[0]
updated_string1 = first_of_string1 + string1[1:]
updated_string2 = first_of_string2 + string2[1:]

combined_string = f'{updated_string1} {updated_string2}'
print(combined_string)
