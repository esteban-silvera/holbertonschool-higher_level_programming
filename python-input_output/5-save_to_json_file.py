#!/usr/bin/python3
"""only define a functions"""
import json
def save_to_json_file(my_obj, filename):
    """only define a functions"""
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
