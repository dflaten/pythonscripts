#!/usr/bin/env python3

'''
Counter is a tool that supports fast tallies of things.
'''

from collections import Counter


# For example we can count characters
counter = Counter('critical')
print(counter)
print(counter["c"])

# Return an iterable of the items in the counter
print(list(counter.elements()))
# Returns the top recurring "n" items
print(counter.most_common(2))

# Testing the subtract method which will subtract
# the occurences in one counter from another 
# mapping or iterable.
counter_one = Counter("superfluous")
print(counter_one)

counter_two = Counter("super")
print(counter_one.subtract(counter_two))

print(counter_one)