#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for fila in matrix:
        new_fila = []
        for valor in fila:
            new_fila.append(valor * valor)
        matrix.append(new_fila)
    return matrix2
