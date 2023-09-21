#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number * +1
x = n %10
if x != 0:
    if number < 0:
        x = -x
        print(f"Last digit of {number} is {x} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {x} and is greater than 5")
else:
    print(f"Last digit of {number} is {x} and is 0")
