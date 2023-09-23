#!/usr/bin/python3
for numero in range(1, 100):
    if numero == 99:
        print("{}".format(numero))
    else:
        print("{:02}".format(numero), end=", ")
