#!/usr/bin/python3
def uniq_add(my_list=[]):
    lista = []
    suma = 0
    for num in my_list:
        if num not in lista:
            lista.append(num)
            suma += num
    return suma
