#!/usr/bin/python3
"""solo un rectangulo mi rey"""
import json
class Base:
    """solo un rectangulo mi rey"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id =  type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
