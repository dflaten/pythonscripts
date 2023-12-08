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

set_1 = {0,1,2,3,4,5}
set_1_but_more = {1,2,3,4,5,6,7}
set_2 = {'a','b','c'}
# You can preform set theory operations in Python from mathematics:
# Union
print(set_1.union(set_2))
# Intersection
print(set_1.intersection(set_1_but_more))
# Difference
print(set_1.difference(set_1_but_more))
