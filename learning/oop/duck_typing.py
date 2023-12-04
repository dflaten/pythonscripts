#!/usr/bin/env python3

# Duck Typing - Python follows the convention that if an object has the required methods you 
# do not need to explictly inherit a class in order for the object to be treated like it has. 

# For example below: both the Duck and the Goose have the 'Speak' method defined so the 
# BirdSound class can take either of them as a parameter to its 'Sound' method.
class Duck:
    def Speak(self):
        print("Quack!")

class Goose:
    def Speak(self):
        print("Honk!")

class BirdSound:
    def Sound(self, bird):
        bird.Speak()

bird_sound = BirdSound()
duck = Duck()
goose = Goose()

bird_sound.Sound(duck)
bird_sound.Sound(goose)