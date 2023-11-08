#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_matrix = matrix.copy()
    i= 0 
    j= 0 
    while j < len(nw_matrix):
        while i <len(nw_matrix[j]):
            nw_matrix[j][i] = nw_matrix[j][i] ** 2
            i+=1
        j+= 1
    return nw_matrix
