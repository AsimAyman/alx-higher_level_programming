#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_matrix =[[e ** 2 for e in r ]for r in matrix]
    return nw_matrix
