#!/usr/bin/python3
"""only define a functions"""
import json
def load_from_json_file(filename):
    """only define a functions"""
    with open(filename, mode='r') as file:
        data = json.load(file)
    return data