#!/usr/bin/python3
"""only define a functions"""
import json
def from_json_string(my_str):
    """only define a functions"""
    try:
        return json.loads(my_str)
    except json.JSONDecodeError:
        return None
