#!/usr/bin/python3
for letra in range(97, 123):
    if chr(letra) not in "e" and chr(letra) not in "q":
        print(chr(letra), end='')
