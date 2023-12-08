#!/usr/bin/env python3

'''
Set - A set in Python is an unordered collection of data items. It is not indexed and
so can be thought of as a bag of random items. Mutable data structures like lists or
dicts can not be added to a set but tuples can be.

Uses: sets are useful for removing duplicates from a list or other structure since you 
can not store duplicates in a set. 
'''

#create empty set
a_set = set()

#intialize set with values
b_set = set({"Something", 123, (456, 789)})

a_set.add("a thing")
a_set.add("another")

#can't add duplicates
a_set.add("a thing")
b_set.add(123)
b_set.remove("Something")

print(a_set)
print(b_set)