#!/usr/bin/env python3

class Vehicle:
    fuelMax = 100
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def printDetails(self):
        print("Manufacturer: " , self.make)
        print("Model: " , self.model)
        print("Color: ", self.color)

# Here we are creating a car that inherits methods and parameters from Vehicle
class Car(Vehicle):
    fuelMax = 60
    def __init__(self, make, model, color, doors):
        #Super can be used to user the initializer from the Parent class to help
        #create your child class
        super().__init__(make, model, color)
        self.doors = doors
    
    def printCarDetails(self):
        self.printDetails()
        print("Doors: ", self.doors)

    def displayFuelMax(self):
        print("Fuel max for a generic vehicle is: ", super().fuelMax)
        print("Fuel max for this car is: ", self.fuelMax)

class HybridCar(Car):
    fuelMax = 90
    def __init__(self, make, model, color, doors):
        super().__init__(make, model, color, doors)
    def enableFullElectricMode(self):
        print("UNLIMITED POWAAAA!!!!!")

myCar = Car("Toyota", "Camry", "2019", 4)
myCar.printCarDetails()
myCar.displayFuelMax()
print()
myHybrid = HybridCar("Toyota", "Prius", 2039, 5)
myHybrid.printCarDetails()
myHybrid.enableFullElectricMode()

print()
print()

class CombustionEngine():  
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine():  
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()