#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ed in matrix:
        for gar in ed:
            print("{:d}".format(gar), end=' ' if gar != ed[-1] else '')
        print()
