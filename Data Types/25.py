# 25. Write a Python program to check whether all dictionaries in a list are empty or
# not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

lst = [{}, {}, {}]
print(all(not i for i in lst))
