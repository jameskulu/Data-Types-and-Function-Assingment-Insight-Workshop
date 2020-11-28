# 16. Write a Python program to square and cube every number in a given list of
# integers using Lambda.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squared_lst = list(map(lambda x: x*x, lst))
cubed_lst = list(map(lambda x: x*x*x, lst))
print(f'Squared list is {squared_lst}')
print(f'Cubed list is {cubed_lst}')
