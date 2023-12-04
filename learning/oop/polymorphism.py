#!/usr/bin/env python3

# One draw back of the following implementation is that we are not strictly requiring the shapes to define the `getArea()` function.
# To do so you want to use abstract classes, see abstract_classes.py for details.
class Shape:
    def __init__(self):
        self.sides = 0

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