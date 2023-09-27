#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary)
    for formato in new:
        print("{}: {}".format(formato, a_dictionary.get(formato)))
