#!/usr/bin/env python3
from collections import defaultdict
'''
defaultdict is a subclass of Python's dict.It automatically assigns 
zero as the value to any key that is not in it.
'''

sentence = "The red for jumped over the fence and ran to the zoo for food"

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

reg_dict = {}
for word in words:
    if word in reg_dict:
        reg_dict[word] += 1
    else:
        reg_dict[word] = 1

print("-----------------------")
print(reg_dict)
print("-----------------------")

#Using default dict this is much simpler:

d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)
print("-----------------------")

# You can pass a type, function or lambda imto the constructor
# for the default dicct
my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

d_with_list = defaultdict(list)
for acct_num, value in my_list:
    d_with_list[acct_num].append(value)

print(d_with_list)
print("-----------------------")
# Here we use a lambda to assign a default value to any item 
# in the dict
animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'

print (animal['Nick'])

print (animal)