#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if isinstance(a, int) and isinstance(b, int):
            mod = a / b
    except:
        return None
    finally:
        print("Inside result: {}".format(mod))
        return mod
    