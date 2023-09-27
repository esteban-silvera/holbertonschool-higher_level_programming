#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    lista = []
    for elemento in set_1:
        if elemento not in set_2:
            lista.append(elemento)
    return lista
