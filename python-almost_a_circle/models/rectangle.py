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
        return self.__height
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def y(self):
        return self.__y
    @y.setter    
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """imprime el rectangulo"""
        for forma in range(self.height):
            print("#" * self.width)

    def __str__(self):
        print("[Rectangle] ({}) {}/{} - {}/{}".format(self.__init__(id), self.__x, self.__y, self.__width, self.__height))
