#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for fila in matrix:
        new_fila = []
        for valor in fila:
            new_fila.append(valor * valor)
        matrix.append(new_fila)
    return matrix2

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
