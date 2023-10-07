#!/usr/bin/python3
"""un objeto de base mi rey"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry  

class Rectangle(BaseGeometry):
    """una base mi rey"""
    
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        areovic = self.__width * self.__height 
        return areovic

    def __str__(self):
        textito = "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return textito
