#!/usr/bin/python3
def add_integer(a, b=98):
    """
    una funcion que retorna rey
    """
    if a is int or b is int:
        return a + b
    elif a is float or b is float:
        if a is float:
            a_int = int(a)
        elif b is float:
            b_int = int(b)
        return b + a                
    if a is not int:
        raise print("a must be an integer")
    else:
        raise print("b must be an integer")