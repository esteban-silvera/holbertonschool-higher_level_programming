#!/usr/bin/python3
for numero in range(0, 100):
    if numero == 99:
        print("{}\n".format(numero))
    else:
        print("{:02}".format(numero), end=", ")
