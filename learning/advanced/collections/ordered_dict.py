#!/usr/bin/env python3
from collections import OrderedDict
'''
This is useful when you need your dictionary to have a sorted order
by the keys. Note that when you add new items to the OrderedDict they
will be appended to the end and you will need to resort them in order
for them to stay ordered. 
'''
# Sorting a regular dict
d = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
keys = d.keys()
print(keys)


keys = sorted(keys)
print(keys)


for key in keys:
    print(key, d[key])

print("----------------")
# Using an OrderedDict
d = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
new_d = OrderedDict(sorted(d.items()))
print(new_d)


for key in new_d:
    print(key, new_d[key])