#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_matrix = matrix.copy()
    i = 0
    while i < len(nw_matrix):
        j = 0
        while j < len(nw_matrix[i]):
            nw_matrix[i][j] = nw_matrix[i][j] ** 2
            j += 1
        i += 1
    return nw_matrix
