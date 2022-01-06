#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_arm = []
    for i in range(len(matrix)):
        new_arm.append([])
        for o in matrix[i]:
            new_arm[i].append(o ** 2)
    return new_arm
