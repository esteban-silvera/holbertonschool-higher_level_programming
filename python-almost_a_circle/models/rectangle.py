#!/usr/bin/python3
"""solo un rectangulo mi rey"""
from models.base import Base
class Rectangle(Base):
    """solo un rectangulo mi rey"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
