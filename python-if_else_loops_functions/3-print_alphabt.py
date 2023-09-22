#!/usr/bin/python3
for letra in range(97, 123):
    if chr(letra) not in ['e', 'q']:
        print(chr(letra), end='')
