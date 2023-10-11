#!/usr/bin/python3
"""only a functions"""
def append_write(filename="", text=""):
    """only define a functions"""
    x = 0
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        x = len(text)
    return x
