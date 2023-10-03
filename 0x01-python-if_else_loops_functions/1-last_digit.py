#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])

# print("Last digit of", number, "is", lastdigit, end=" ")

if lastdigit > 5:
    print("Last digit of", number, "is", lastdigit, "and is greater than 5", end=" ")
if lastdigit == 0:
    print("Last digit of", number, "is", lastdigit, "and is 0", end=" ")
if lastdigit < 6 and not 0:
     print("Last digit of", number, "is", lastdigit, "and is less than 6 and not 0", end=" ")
