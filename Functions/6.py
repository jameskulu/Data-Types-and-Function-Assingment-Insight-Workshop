# 6. Write a Python function to check whether a number is in a given range.


def check_num_in_range(num):
    ran = range(1, 20)
    if num in ran:
        print("Number is in a given range")
    else:
        print("Number is not in a given range")


check_num_in_range(10)
