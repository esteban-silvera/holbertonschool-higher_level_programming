#!/usr/bin/python3
"""solo un rectangulo mi rey"""
class Base:
    """solo un rectangulo mi rey"""
    def __init__(self, id=None):
        self.__nb_objects = 0
        if id is not None:
            self.__id = id
        else:
            type(self).__nb_objects += 1
            self.__id =  type(self).__nb_objects
