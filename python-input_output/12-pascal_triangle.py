#!/usr/bin/python3
"""only define a functions"""
def pascal_triangle(n):
    """only define a functions"""
    listorti = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        escalon = [1]
        centro = listorti[i - 1]
        escalon.extend([sum(pair) for pair in zip(centro, centro[1:])])
        escalon.append(1)
        listorti.append(escalon)
    return listorti
