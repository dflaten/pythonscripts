#!/usr/bin/env python3

# Implement a Class Point that has 3 properties and a method. All public. Point should
# accept 3 numbers in the initializer and method should square the 3 numbers and sum
# them returning the result.
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def sumOfSquares(self):
        return (self.x * self.x) + (self.y * self.y) + (self.z * self.z)

a = Point(1,2, 3)

print("Sum of Squares for a: ", a.sumOfSquares())

# Implement a class, Student that has 4 properties and two methods. 
# Properties include the name of the student and the scores for 3 classes.
# Methods calculate the total scores obtained and the percentage of those scores
class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
    
    def totalObtained(self):
        return self.phy + self.chem + self.bio
    
    def percentage(self):
        return (self.totalObtained() / 300) * 100

student = Student("Atla", 60, 80, 99)
print("My student: ", student.name)
print("Her percentage: ", student.percentage())

# Create a Calculator class that can take two numbers and preform
# `add()`, 'subtract()', 'multiply()`, and 'divide()' on those numbers.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self): 
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self): 
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2

myCalc = Calculator(1,2)

print("Calculator oprations on 1, 2:")
print ("Add: ", myCalc.add())
print ("Subtract: ", myCalc.subtract())
print ("Multiply: ", myCalc.multiply())
print ("Divide: ", myCalc.divide())