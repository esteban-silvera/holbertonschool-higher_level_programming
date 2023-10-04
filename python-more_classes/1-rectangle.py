#!/usr/bin/python3
"""
	Module 0-rectangle
	Defines rectangle class
"""
class Rectangle:
    """solo un rectangulo mi rey"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        ancho = self.width
        return ancho
    
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    def height(self):
        alto = self.height
        return alto

    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
