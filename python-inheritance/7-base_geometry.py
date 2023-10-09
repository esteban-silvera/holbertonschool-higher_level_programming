#!/usr/bin/python3
"""un objeto de base mi rey"""
class BaseGeometry:
    """una base mi rey"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
