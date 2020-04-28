#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    Last_Number = number % 10
else:
    Last_Number = number % -10
print("Last digit of {:d} is {:d} and is".format(number, Last_Number), end=" ")
if Last_Number > 5:
    print("greater than 5")
elif Last_Number == 0:
    print("0")
else:
    print("less than 6 and not 0")
