#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lista2 = [x for x in my_list]
    if idx < 0 or idx > (len(my_list) - 1):
        return lista2
    lista2[idx] = element
    return lista2
