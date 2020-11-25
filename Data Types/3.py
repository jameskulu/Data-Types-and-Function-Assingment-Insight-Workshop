# 3. Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t

string = input("Enter a string: ")
first_letter = string[0]
if first_letter in string:
    replaced_by_dollor = string[1:].replace(first_letter, "$")
    print(first_letter + replaced_by_dollor)
