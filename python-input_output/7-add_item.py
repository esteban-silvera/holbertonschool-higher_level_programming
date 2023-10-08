#!/usr/bin/python3
"""only define a functions"""
import json
import sys
import os
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
"""only define a functions"""

load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file
"""only define a functions"""

def main():
    """only define a functions"""
    filename = "add_item.json"
    if not os.path.exists(filename):
        save_to_json_file([], filename)
    my_list = load_from_json_file(filename)
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
