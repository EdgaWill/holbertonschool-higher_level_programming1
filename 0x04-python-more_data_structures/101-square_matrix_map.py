#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda est: list(map(lambda a: a**2, est)), matrix))
