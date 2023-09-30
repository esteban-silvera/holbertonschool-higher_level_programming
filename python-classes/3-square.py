#!/usr/bin/python3
"""
	Module 0-square
	Defines class Square
"""
class Square:
    """solo un cuadrado mi rey"""
    pass
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        areovic = self.__size ** 2
        return areovic