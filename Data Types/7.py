# 7. Write a Python function that takes a list of words and returns the length of the
# longest one.

list_of_words = ['hey', 'hy', 'hello', 'bye']
longest = list_of_words[0]

for i in list_of_words:
    if len(longest) < len(i):
        longest = i

print(f'The longest word in this list is "{longest}".')
