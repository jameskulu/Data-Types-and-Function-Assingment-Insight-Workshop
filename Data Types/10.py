# 10. Write a Python program to remove the characters which have odd index
# values of a given string.

string = input("Enter a string: ")
new_string = ''
for i in range(len(string)):
    if i % 2 == 0:
        new_string = new_string + string[i]
print(new_string)
