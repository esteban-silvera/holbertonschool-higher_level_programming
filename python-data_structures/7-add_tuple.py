#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    nuevo = 0, 0
    if len(tuple_a) < 2:
        tuple_a = tuple_a + nuevo
    if len(tuple_b) < 2:
        tuple_b = tuple_a + nuevo

    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result_tuple
    