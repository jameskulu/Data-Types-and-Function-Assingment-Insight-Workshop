# 11. Write a Python program to count the occurrences of each word in a given sentence.

sentence = 'Python is the best programming language ever and this language is the famous programming language'
splited_sentence = sentence.split()
dict = {}

for i in splited_sentence:
    dict[i] = splited_sentence.count(i)

print(dict)
