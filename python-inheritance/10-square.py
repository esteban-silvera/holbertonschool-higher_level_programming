#!/usr/bin/python3
"""un objeto de base mi rey"""
Rectangle = __import__("9-rectangle").Rectangle
class Square(Rectangle):
    """una base mi rey"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
