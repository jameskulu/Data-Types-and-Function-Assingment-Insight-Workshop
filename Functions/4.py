# 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"


def reverse_func(string):
    rev_string = string[::-1]
    return rev_string


string = 'james'
print(reverse_func(string))
