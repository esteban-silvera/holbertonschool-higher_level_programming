#!/usr/bin/python3
"""
	Module 0-rectangle
	Defines rectangle class
"""
class Rectangle:
    """solo un rectangulo mi rey"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        ancho = self.__width
        return ancho

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        alto = self.__height
        return alto

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        aerovic = self.__height * self.__width
        return aerovic

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            nerimetro = 2 * (self.__height + self.__width)
            return nerimetro

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.__height):
                rectangle_str += "#" * self.__width + "\n"
            return rectangle_str[:-1] 
    
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
