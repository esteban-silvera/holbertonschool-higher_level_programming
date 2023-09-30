#!/usr/bin/python3
"""
	Module 0-square
	Defines class Square
"""
class Square:
    """solo un cuadrado mi rey"""
    pass
    def __init__(self, size=0):
        if size is int:
            if size > 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
