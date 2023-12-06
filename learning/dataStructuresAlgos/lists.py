#!/usr/bin/env python3
'''
Lists in python are very simple. Just `[]` to create a list.

You can even mix in different types and imbed lists in other lists.
'''

items = ["teddy bear", "ball", "doll", "40"]
embedded_list_example = [[1,2,3], [4,5,6]]
print(items)
print(embedded_list_example)

#Can combine lists and access sublists like tthis

combined_list = embedded_list_example[0] + embedded_list_example[1]
print(combined_list)

#Access items in an embedded list
print("Printing 3: " , embedded_list_example[0][2])

#Adding an item to a list
combined_list.append(7)
print(combined_list)

#inserting and item
combined_list.insert(0,0)
print(combined_list)

#removing an item
combined_list.remove(0)
print(combined_list)

#iterating through list
for number in combined_list:
    print(number)

list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

# This creates tuples out of the values in the two lists when their sum is > 100
sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]


print(sum_list)
