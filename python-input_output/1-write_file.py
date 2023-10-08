#!/usr/bin/python3
"""only a functions"""
def write_file(filename="", text=""):
    """only define a functions"""
    x = 0
    with open(filename, encoding="utf-8") as text:
        for letra in text:
            x += 1
        return x
