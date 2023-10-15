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
        """Convertineitor 30000."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """sacame una foto run acelera run."""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json_string)
