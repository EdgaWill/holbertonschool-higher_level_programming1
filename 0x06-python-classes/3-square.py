#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a squares"""
    def __init__(self, size=0):
        """size is size of elements"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """genera"""
        return self.__size ** 2
