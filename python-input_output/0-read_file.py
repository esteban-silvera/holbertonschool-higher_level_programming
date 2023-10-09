#!/usr/bin/python3
"""only a functions"""
def read_file(filename=""):
    """only define a functions"""
    with open(filename, encoding="utf-8") as fd:
        for line in fd:
            print(line, end="")
