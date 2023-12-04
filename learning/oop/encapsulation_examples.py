#!/usr/bin/env python3

class User:
    def __init__(self, username=None):
        self.__username = username
    def setUserName(self, username):
        self.__username = username
    def getUserName(self):
        return self.__username

newUser = User()
newUser.setUserName("its-a-me")
print("Username: ", newUser.getUserName())

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def area(self): 
        return self.__length * self.__width
    
    def perimeter(self):
        return (self.__length * 2) + (self.__width * 2)

square = Rectangle(2, 2)
longRectangle = Rectangle(100, 5)

print("Area for square is: " , square.area())
print("Area for long rectangle is: " , longRectangle.area())

print("Perimeter for square is: " , square.perimeter())
print("Perimeter for long rectangle is: " , longRectangle.perimeter())

class Student:
    def __init__(self, name=None, rollNumber=None):
        self.__name = name;
        self.__rollNumber = rollNumber
    
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    
    def getRollNumber(self):
        return self.__rollNumber

mario = Student()
mario.setName("Mario")
mario.setRollNumber(1)

print("My Student:", mario.getName(), " Roll Number: ", mario.getRollNumber())