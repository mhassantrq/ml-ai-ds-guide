"""
The random module is used to generate random values.
"""

import random


#   generate a random number between given range with gaps
var = random.randrange(5, 15, 2)     #   random between 5 and 15 with gap of 2, so numbers like 7, 9, 11 etc.
print(var)


#   generate a random float number between 0 and 1
var = random.random()
print(var)


#   generate a random float number between given range
var = random.uniform(5, 15)     #   random int between 5 and 15
print(var)


#   generate a random int number between given range
var = random.randint(5, 15)     #   random int between 5 and 15
print(var)
