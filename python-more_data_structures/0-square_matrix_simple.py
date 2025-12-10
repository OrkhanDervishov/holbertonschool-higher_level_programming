#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in matrix:
        row = []
        for j in i:
           row.append(j*j)
        square_matrix.append(row)
    return square_matrix
