#!/usr/bin/python3
"""
	Module 0-square
	Defines class Square
"""
class Square:
    """solo un cuadrado mi rey"""
    
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        lado = self.__size
        return lado

    @size.setter
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
        lado = self.__size
        for x in range(0, self.__size):
            for n in range(lado):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
