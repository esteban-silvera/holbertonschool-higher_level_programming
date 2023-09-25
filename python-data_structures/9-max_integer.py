#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    maximo = 0
    for num in my_list:
        if num > maximo:
            maximo = num
    return (maximo)