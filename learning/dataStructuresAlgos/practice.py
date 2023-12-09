#!/usr/bin/env python3
'''
You are given a list called my_list. Using this list, you must create a tuple called my_tuple. 
The tuple will contain the list’s first element, last element, and the length of the list, in that same order.
'''

my_list = [55, 91.1, "Harry Potter", 21, "Bolvar"]

def listDescriber(a_list):
    first = a_list[0]
    last = a_list[len(a_list) - 1]
    length = len(a_list)
    return (first, last, length)

print("The first element, last element, and size of ", my_list, " is: ",listDescriber(my_list))

'''
Given a list of integers and a number k, find the kth largest integer in the list. 
'''
list_of_ints = [89, 1, 3,134, 73, 23]
k = 3

def determineKthLargest(a_list, k):
    a_list.sort()
    return a_list[k]

print("The ", k, "th largest number in this list: ", list_of_ints, " is: ", determineKthLargest(list_of_ints, k))

'''
Given a list of numbers return an array consisting of two elements the number of high numbers and
the number of low numbers where a number is high if it is greater than 50 or divisible by 3 and 
low if not.
'''
another_list_of_ints = [12, 5, 43, 156, 73, 33, 3333, 45, -3]

def count_low_high(num_list):
    low = 0
    high = 0
    for number in num_list:
        if number % 3 == 0 or number > 50:
            high += 1
        else:
            low +=1
    return [low, high]

print("The number of low and high numbers in this array: ", another_list_of_ints, " is: ", count_low_high(another_list_of_ints))
