#!/usr/bin/python3
"""
	Module 0-square
	Defines class Square
"""
class Square:
    """solo un cuadrado mi rey"""
    
    def __init__(self, size=0):
        self.size = size

    def size(self):
        lado = self.__size
        return lado

    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        areovic = self.__size ** 2
        return areovic

    def my_print(self):
        for x in range(0, self.__size):
            [print("#", end="") for n in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
