#!/usr/bin/python3
"""only a functions"""
def append_write(filename="", text=""):
    """only define a functions"""
    x = 0
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
        texto = ""
        for char in text:
            texto += char
            x += 1
    return x, texto
