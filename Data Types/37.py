# 37. Write a Python program to multiply all the items in a dictionary.

dct = {
    '1st': 10,
    '2nd': 65,
    '3rd': 54,
    '4th': 32,
    '5th': 79
}

mul_of_dst = 1

for key, items in dct.items():
    mul_of_dst *= items

print(mul_of_dst)
