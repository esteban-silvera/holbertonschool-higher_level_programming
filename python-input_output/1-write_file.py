#!/usr/bin/python3
"""only a functions"""
def write_file(filename="", text=""):
    """only define a functions"""
    with open(filename, encoding="utf-8") as content:
        content.write(text)
        return len(text)
