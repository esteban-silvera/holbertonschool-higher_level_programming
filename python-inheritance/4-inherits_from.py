#!/usr/bin/python3
"""is a function"""
def inherits_from(obj, a_class):
    """is a function"""
    if (type(obj) != a_class):
        return issubclass(type(obj), a_class)
    return False
