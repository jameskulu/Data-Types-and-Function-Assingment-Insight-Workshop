# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336


def multiplication_of_list(lst):
    mul = 1
    for i in lst:
        mul *= i
    return mul


print(multiplication_of_list([8, 2, 3, -1, 7]))
