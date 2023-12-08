#!/usr/bin/env python3
'''
Dictionaries are key-value pairs where each unique key is an index
that holds the value associated with it.
'''

super_hero_mot = {"Batman": "batmobile",
                  "Superman": "supermobile",
                  "Superwoman": "invisible jet"}

print(super_hero_mot)

# adding item
super_hero_mot["Robin"] = "motorcycle"

# removing
del super_hero_mot["Superman"]
print(super_hero_mot)

# checking for existance
print("Batman" in super_hero_mot)

#iteration
for (superhero, mode_of_transportation) in super_hero_mot.items():
    print("Hero: " + superhero + ", Mode of Transportation: " + mode_of_transportation)