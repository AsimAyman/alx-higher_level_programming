#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return (list(map(lambda inerlist: list(map(lambda e: e**2, inerlist)),matrix)))
