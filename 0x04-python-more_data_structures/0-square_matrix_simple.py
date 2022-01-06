#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_arm = []
    for a in range(len(matrix)):
        new_arm.append([])
        for t in matrix[a]:
            new_arm[a].append(t ** 2)
    return new_arm
