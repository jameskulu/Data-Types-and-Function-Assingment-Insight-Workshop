# 8. Write a Python program to remove the nth index character from a nonempty string.

try:
    string = input("Enter a string: ")
    index_from_user = int(input("Enter an index to remove: "))

    if index_from_user < len(string):
        new_string = string.replace(string[index_from_user], "", 1)
        print(new_string)
    else:
        print("Index out of range.")
except(Exception):
    print("cannot take string value")
