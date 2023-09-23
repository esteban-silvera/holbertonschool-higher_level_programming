#!/usr/bin/python3
def uppercase(str):
    texto = ""
    for letra in str:
        if 97 <= ord(letra) <= 122:
            texto += chr(ord(letra) - 32)
        else:
            texto += letra
    print(f"{texto}", "")
