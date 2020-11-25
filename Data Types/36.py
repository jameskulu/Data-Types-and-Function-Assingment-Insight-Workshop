# 36. Write a Python program to sum all the items in a dictionary.

dct = {
    '1st': 10,
    '2nd': 65,
    '3rd': 54,
    '4th': 32,
    '5th': 79
}

sum_of_dst = 0

for key, items in dct.items():
    sum_of_dst += items

print(sum_of_dst)
