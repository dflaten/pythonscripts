#!/usr/bin/env python3
# Basic Class implementation in Python.
import random
class Employee:
    # This is a shared class value that all instances share. If any instances
    # change this field they will all change so be careful with these.
    company = 'ACME'
    # this is kind of a constructor if you are thinking in terms of Java
    # default values are set in the parameters with the = sign

    def __init__(self, salary=0, department=None):
        self.ID = self.__generateID()
        # Here Salary is a Private variable, if you want to give access to the 
        # value you would need to create getters/setters. 
        self.__salary = salary 
        self.department = department 

    def __generateID(self):
        """
        Method for generating an id for an employee at random. This is a private
        method in the class. 
        """
        return random.randint(0,1000)

    @classmethod
    def getCompanyName(cls):
        """
        Here we are defining a class method that is available to all methods in the 
        class. By convention 'cls' is used to refer to the class. You can name this
        whatever you like though.
        """
        return cls.company
    
    @staticmethod
    def staticDemo():
        """
        Static methods like this one can't modify the class and don't know anything
        about its state (hence being static)
    @staticmethod
        """
        print("I am a static method!")
    
    
    def tax(self):
        """
        Calculates the tax the employee owes.
        Parameters:
        ----
        self : Employee
          The employee

        Returns:
        ------
        float
           The tax owed
        """
        return (self.__salary * 0.2)
    
    def salaryPerDay(self): 
        """
        Calculates the salary per day the employee makes, assumes
        the salary is paid out every 30 days.

        Parameters:
        ----
        self : Employee
          The employee

        Returns:
        ------
        float
           The salary amount in dollars per day. 
        """
        return (self.__salary / 30)
    def demo(self, a, b, c, d=5, e=None):
        """
        Shows how "method overriding" ran be preformed in Python.
        You essentially define default parameters which could sometimes
        be excluded to allow different values to be assigned to the variable.

        Method overriding saves memory and code since you don't need to create
        another method to handle different parameters.
        """
        print("a=", a)
        print("b=", b)
        print("c=", c)
        print("d=", d)
        print("e=", e)

frank = Employee(4000,"Engineering")
john = Employee()
print("Frank ID: ", frank.ID)
print("Frank company: ", frank.company)
print("John ID: ", john.ID)
print("John company: ", john.company)

# you can also add additional fields outside the class like:
frank.title = "Software Engineer"
print("Frank Title: ", frank.title)

print("Frank salary per day: ", frank.salaryPerDay())

# method overrriding:
print("Demo 1")
frank.demo(1,2,3)
print("Demo 2")
frank.demo(1,2,3,4)