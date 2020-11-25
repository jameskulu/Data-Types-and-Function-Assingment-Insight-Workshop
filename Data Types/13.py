# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).


def sort(lst):
    lst = [str(i) for i in lst]
    lst.sort()
    lst = [int(i) if i.isdigit() else i for i in lst]
    return lst


user_inputted_string = input('Enter comma seperated words: ')
list_of_words = set(user_inputted_string.split(','))
print(sort(list_of_words))
