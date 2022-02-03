#!/usr/bin/python3
"""module to instantiate objects
        Class:
            BaseGeometry
"""


Rectangle = __import__("9-rectangle").Rectangle
""" Import module
"""


class Square(Rectangle):
    """ Class definition
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
