#!/usr/bin/python3
def uppercase(str):
    for letra in str:
        if 97 <= ord(letra) <= 122:
            letra = chr(ord(letra) - 32)
        print("{}".format(letra), end="")
    print("")
