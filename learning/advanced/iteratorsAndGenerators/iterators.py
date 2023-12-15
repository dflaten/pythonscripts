#!/usr/bin/env python3
from itertools import count
from itertools import islice
from itertools import chain 
from itertools import dropwhile
from itertools import filterfalse

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
    # Other methods are available like cycle which will
    # allow you to continously cycle through a list of things.
    # Repeat will return the same thing over and over again, similiar
    # to a cycle but with just one item and only for as many times as you 
    # pass into it.


    '''
    If you want to take a series of iterables and flatten them into one long
    iterable you can use the chain method like so:
    '''

    first_list = ['one', 'two']
    print('First List before combining: ', first_list)
    numbers = list(range(7))
    things = ['thing 1', 'thing 2']

    first_list = list(chain(first_list, numbers, things))
    print('First List after combining: ', first_list)
    print('----------------')
    '''
    Dropwhile is used to filter out a set of records based on a condition:

    This drops values until a value in the list doesn't meet the condition.
    '''
    print(list(dropwhile(lambda x: x < 3, [1,2,3,4,5,7,0])))

    '''
    filterfalse can be used to actually filter all elements that evaluate to false:
    '''
    def greater_than_five(x):
        return x > 5 

    print (list(filterfalse(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10, 1, 2])))
    print('----------------')

    '''
    groupby is very useful for returning consecutive keys and groups from an iterable.
    '''
    from itertools import groupby

    vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durango'),
                ('Chevrolet', 'Cobalt'), ('Ford', 'F150'),
                ('Dodge', 'Charger'), ('Ford', 'GT')]

    # If you don't sort the list before doing the group by method
    # things will not work as expected. The method will not be
    # able to group items correctly.
    sorted_vehicles = sorted(vehicles)

    for key, group in groupby(sorted_vehicles, lambda make: make[0]):
        for make, model in group:
            print('{model} is made by {make}'.format(model=model,
                                                    make=make))
        print ("**** END OF GROUP ***\n")