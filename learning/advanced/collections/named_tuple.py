#!/usr/bin/env python3
from collections import namedtuple
'''
A named tuple can be used like a struct.

It allows you to create structs easily from things like a database
and you can use arguments like renmae to rename your named tuple
properties if the source is a database or somewhere else.
'''

Parts = namedtuple("Parts", "id_num desc cost amount")

my_auto_parts = Parts(id_num="123", desc= "Radiator",cost=59.99, amount=5 )

print("-----------------")
print(my_auto_parts)
print(my_auto_parts.id_num)
print("-----------------")
# We can also convert a dictionary into a named tuple (or struct if you 
# like to think that way)
parts_dict = {'id_num':'1234', 'desc':'Ford Engine',
     'cost':1200.00, 'amount':10}
parts = namedtuple('Parts', parts_dict.keys())(**parts_dict)
print (parts)
print("-----------------")