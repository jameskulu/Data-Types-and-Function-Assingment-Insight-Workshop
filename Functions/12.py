# 12. Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

import random


def multiply_func(x):
    unknown_number = random.randint(1, 50)
    return x * unknown_number


print(multiply_func(10))
