#!/usr/bin/python3
"""only define a functions"""
import json
def save_to_json_file(my_obj, filename):
    """only define a functions"""
    with open(my_obj, 'w') as file:
        json.dump(filename, file)
