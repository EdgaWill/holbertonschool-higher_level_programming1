#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines square area
    """
    def __init__(self, size=0):
        """Initilizes"""
        self.__size = size

    @property
    def size(self):
        """the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area"""
        return self.__size ** 2
