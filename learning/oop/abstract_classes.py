#!/usr/bin/env python3
from abc import ABC, abstractmethod

# Because we specified that the Shape class requires the `getArea()` method to be implemented
# if we remove the getArea() function from either the Rectangle or the circle it will not compile.
class Shape(ABC):

    @abstractmethod
    def getArea(self):
        pass

# A rectangle is a 'Shape' that implements the getArea function
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sides = 4
    
    def getArea(self):
        return (self.width * self.height)

# A circle is also a 'Shape' that implements the getArea function
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.sides = 0
    
    def getArea(self):
        return (self.radius * self.radius * 3.142)

circle = Circle(2)
rectangle = Rectangle(3,4)

print("Radius of circle: ", circle.getArea())
print("Radius of rectangle: ", rectangle.getArea())

        