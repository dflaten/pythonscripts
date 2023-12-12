#!/usr/bin/env python3
from collections import deque
import string
'''
deques (pronounced decks) are double-ended queues that are a
replacement for a Python list. They are thread-safe and support
memory efficient appends and pops from either side of the deque.

In general if we need fast appends or fast pops, use a dequeu. If
you need fast random access use a list.
'''

d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)
# Append to the back of the queue
d.append("work")
print(d)
# Append to the front of the queue
d.appendleft("now")
print(d)
# Rotates the queue one to the right
# If you pass it a negative number it will rotate to the left.
d.rotate(1)
print(d)