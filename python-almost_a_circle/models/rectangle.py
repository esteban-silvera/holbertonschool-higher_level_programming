#!/usr/bin/python3
"""solo un rectangulo mi rey"""
from models.base import Base
class Rectangle(Base):
    """solo un rectangulo mi rey"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def height(self):
        altura = self.height
        return altura

    @height.setter
    def def_height(self, height):
        if height is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height


    @property
    def width(self):
        ancho = self.width
        return ancho

    @width.setter
    def def_width(self, width):
        if width is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width


    @property
    def y(self):
        y = self.y
        return y

    @y.setter    
    def def_y(self, y):
        if y is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y


    @property
    def x(self):
        x = self.x
        return x

    @x.setter
    def def_x(self, x):
        if x is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
