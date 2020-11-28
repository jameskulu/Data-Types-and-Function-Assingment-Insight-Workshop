# 7. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.


string = 'JaMes'
upper_count = 0
lower_count = 0

for i in string:
    if i == i.upper():
        upper_count += 1
    elif i == i.lower():
        lower_count += 1

print(f'Uppercase letters is {upper_count}')
print(f'Lowercase letters is {lower_count}')
