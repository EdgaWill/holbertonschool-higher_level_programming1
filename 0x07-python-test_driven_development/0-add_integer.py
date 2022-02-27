#!/usr/bin/python3
'''
    integers addition
'''


def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("a must be an integer")
    return int(a) + int(b)
