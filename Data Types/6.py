# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'


string = 'The lyrics is not that poor!'

if 'not' in string and 'poor' in string:

    index_of_not = string.index("not")
    index_of_poor = string.rindex("r") + 1

    if index_of_poor > index_of_not:
        new_string = string.replace(string[index_of_not:index_of_poor], 'good')
        print(new_string)
else:
    print(string)
