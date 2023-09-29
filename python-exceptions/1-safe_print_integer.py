#!/usr/bin/python3
def safe_print_integer(value):
    try:
        x = False
        if isinstance(value, int):
            x = True
        print("{:d}".format(value))
        return x
    except (ValueError, TypeError):
        return x
