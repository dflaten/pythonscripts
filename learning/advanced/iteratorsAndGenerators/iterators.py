#!/usr/bin/env python3
from itertools import count
from itertools import islice
'''
Iterators must implement a _iter_ and _next_ method.

Lists are not iterators, if you want to use one as an iterator
you must create the iterator first with the iter() method.
'''
class MyCharacterIterator:

    def __init__(self, characters):
        """
        Constructor
        """
        self.characters = characters
        self.position = 0
    
    def __iter__(self):
        """
        Returns self as iterator
        """
        return self
    
    def __next__(self):
        """
        Returns next number in sequence or raises StopExcception
        if end of list has been reached.
        """
        if self.position >= len(self.characters):
            raise StopIteration
        character = self.characters[self.position]
        self.position += 1
        return character 

class Doubler:

    """
    An infinite iterator. These shouldn't be called unless
    you are bounding them like we do with the 5 in the main 
    method below.
    """

    def __init__(self):
        """
        Constructor
        """

        self.number = 0

    def __iter__(self):
        """
        Returns itself as an iterator
        """

        return self

    def __next__(self):
        """
        Doubles the number each time next is called
        and returns it. 
        """

        self.number += 1
        return self.number * self.number


if __name__ == '__main__':

    my_list = [1,2,3]
    my_list_iterator = iter(my_list)
    print(next(my_list_iterator))
    print(next(my_list_iterator))
    print(next(my_list_iterator))
    
    print('-----------------')

    iterator = MyCharacterIterator('123456')
    for character in iterator:
        print (character)

    print('-----------------')

    doubler = Doubler()
    counter = 0

    for number in doubler:
        print (number)
        if counter > 5:
            break
        counter += 1
    
    def doubler_generator():
        """
        Here we are creating our infinit double generator again
        but using a generator to do so. All you need to create 
        a generator is the yield statement. Python automatically
        creates an iterator when this keyword is used.

        If you open a file with the with open key words it will
        essentially turn the file object into a generator.
        """
        number = 2
        while True:
            yield number
            number *= number

    doubler = doubler_generator()
    print (next(doubler))
    print (next(doubler))
    print (next(doubler))
    print (type(doubler))

    print('-----------------')

    # Below we are using the count() method from itertools
    # to create a counting iterator which counts from 10 up.
    for i in count(10):
        if i > 20: 
            break
        else:
            print(i)
    
    print('-----------------')
    print('Iterate through counting iterator from 10 until you have created 10 items')

    # Iterate through your counting iterator from 10 until
    # you have created 10 items.
    for i in islice(count(10), 10):
        print(i)