# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2


l = ['abc', 'xyz', 'aba', '1221', '565', 'xyx', 'ghj']
lst = []
for i in l:
    if len(i) > 1:
        if i[0] == i[-1]:
            lst.append(i)

print(len(lst))
