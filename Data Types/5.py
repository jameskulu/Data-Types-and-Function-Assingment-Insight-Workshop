# Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly


string = input("Enter a string: ")

if len(string) < 3:
    print(string)
else:
    if string[-3:] == 'ing':
        new_string = string.replace('ing', 'ly')
        print(new_string)
    else:
        new_string = string+'ing'
        print(new_string)
