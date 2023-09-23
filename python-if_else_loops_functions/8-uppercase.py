#!/usr/bin/python3
def uppercase(str):
    for letra in str:
        if 97 >= ord(letra) and 122 <= ord(letra):
            print("{}".format(letra + 32, end=("")))
        else:
            print("{}".format(letra, end=("")))
