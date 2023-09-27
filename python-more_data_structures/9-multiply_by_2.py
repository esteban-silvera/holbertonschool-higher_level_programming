#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for number in a_dictionary:
        a_dictionary[number] = a_dictionary.get(number) * 2
    return a_dictionary
