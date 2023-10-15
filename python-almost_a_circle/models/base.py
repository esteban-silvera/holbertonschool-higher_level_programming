#!/usr/bin/python3
"""solo un rectangulo mi rey"""
import json
import os
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

    @staticmethod
    def from_json_string(json_string):
        """desconvertineitor -3000?."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """xreatineitor 60324.com."""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """cargamela todaa paaaa."""
        filename = f"{cls.__name__}.json"
        instances = []
        if not os.path.exists(filename):
            return instances
        with open(filename, 'r') as file:
            json_string = file.read()
            dictionaries = cls.from_json_string(json_string)
            instances = [cls.create(**dictionary) for dictionary in dictionaries]
        return instances
