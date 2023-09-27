#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for format in a_dictionary:
        if format == key:
            del(a_dictionary[key])
    return a_dictionary
