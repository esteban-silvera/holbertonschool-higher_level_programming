#!/usr/bin/python3
def common_elements(set_1, set_2):
    lista = []
    for elemento in set_1:
        if elemento in set_2:
            lista.append(elemento)
    return lista
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
