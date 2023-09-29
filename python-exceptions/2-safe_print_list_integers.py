#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            if isinstance(i, int):
                print("{}".format(my_list[i]), end="")
    except IndexError:
        return i
    else:
        return x
    finally:
        print("")
