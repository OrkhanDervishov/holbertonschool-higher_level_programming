#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number % 10) == 0:
    print(f"{number} and is 0")
elif (number % 10) > 5:
    print(f"{number} and is greater than 5")
else:
    print(f"{number} and is less that 6 and not 0")
