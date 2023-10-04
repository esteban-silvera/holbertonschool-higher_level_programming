#!/usr/bin/python3
"""
	Module 0-rectangle
	Defines rectangle class
"""
class Rectangle:
    """solo un rectangulo mi rey"""
    pass
    def __init__(self, width=0):
        self.width = width

    def __init__(self, height=0):
        self.height = height

    def width(self):
        ancho = self.width
        return ancho
    
    def width(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.width = value

    def height(self):
        alto = self.height
        return alto

    def height(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.height = value
