#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for valor in fila:
            print("{:d}".format(valor), end=" ")
        print()

ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(ejemplo)