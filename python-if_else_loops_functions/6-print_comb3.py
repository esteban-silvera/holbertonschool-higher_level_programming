#!/usr/bin/python3
for numero in range(0, 10):
    for x in range(numero + 1, 10):
        if numero == 8 and x == 9:
            print("{}{}".format(numero, x))
        else:
            print("{}{}".format(numero, x), end=", ")
