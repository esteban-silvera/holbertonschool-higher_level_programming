#!/usr/bin/python3
"""only a functions"""
def write_file(filename="", text=""):
    """only define a functions"""
    x = 0
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
        for char in text:
            x += 1
    return x
