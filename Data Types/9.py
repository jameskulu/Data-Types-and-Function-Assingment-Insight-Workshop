# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.

string = input("Enter a string: ")
first_chars = string[0]
last_chars = string[-1]

final_output = f'{last_chars}{string[1:-1]}{first_chars}'
print(final_output)
