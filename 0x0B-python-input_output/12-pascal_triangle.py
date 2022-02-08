#!/usr/bin/python3
""" module for get list
        Function:
                pascal_triangle
"""


def pascal_triangle(n):
    """ Function definition
    """
    dlist = []
    if n <= 0:
        return dlist
    dlist.append([1])
    for row in range(1, n):
        dlist.append([])
        for b in range(len(dlist[row - 1]) + 1):
            if b == 0 or b == len(dlist[row - 1]):
                dlist[row].append(1)
            else:
                dlist[row].append(dlist[row - 1][b] + dlist[row - 1][b - 1])
    return dlist
