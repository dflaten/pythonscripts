#!/usr/bin/env python3
'''
There are a few ways to get a stack in python.
1. You can implement your own via a list. The nice part about doing
this is you don't have to import anything. The drawback is you have
to write your own class to get the standard methods: pop, push, 
isEmpty, peek. Also the push operation will be O(n) at the worst
case due to how append() works.

2. You can use collections.queue to implement a stack instead of list.
You will still need to implement a class to get all of the methods like
using a list however you will get faster push and pop operations.

3. You can use queue.LifoQueue, this will give you a lot of the 
operations of a stack natively and works well in a multi-threaded
application as it is thread safe. However it does not have a peek() 
operation and the full()/empty() methods will not be super reliable
since they can change right after the method is called. 
'''
from queue import LifoQueue

stack = LifoQueue()

stack.put("First")
stack.put("Second")
stack.put("Third")

print("Stack is full: ", stack.full())
print("Size of stack: ", stack.qsize())
print("Item on top of stack is: ", stack.peek())

print("Removing elements from stack.")
print(stack.get())
print(stack.get())
print(stack.get())
print("Is stack empty?: ", stack.empty())
