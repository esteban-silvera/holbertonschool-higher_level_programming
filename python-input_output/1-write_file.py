#!/usr/bin/python3
"""only a functions"""
def write_file(filename="", text=""):
    """only define a functions"""
    x = 0
    with open(filename, encoding="utf-8") as content:
        for line in content:
            x += 1
        return x
