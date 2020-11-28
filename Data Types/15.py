# 15. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}


def insert_string(outer_string, inner_string):
    outer_first = outer_string[:2]
    outer_last = outer_string[2:4]
    return f'{outer_first}{inner_string}{outer_last}'


print(insert_string('[[]]<<>>', 'Python'))
