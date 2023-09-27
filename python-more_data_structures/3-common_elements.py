#!/usr/bin/python3
def common_elements(set_1, set_2):
    lista = []
    for elemento in set_1:
        if elemento in set_2:
            lista.append(elemento)
    return lista
