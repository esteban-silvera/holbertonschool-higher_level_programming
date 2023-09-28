#!/usr/bin/python3
def roman_to_int(roman_string): 
    if not roman_string or not isinstance(roman_string, str):
        return 0
    cont = 0
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for x, j in zip(roman_string, roman_string[1:]):
        if x not in valores.keys():
            return 0
        elif valores[x] >= valores[j]:
            cont += valores[x]
        else:
            cont -= valores[x]
    cont += valores[roman_string[-1]]
    return cont
