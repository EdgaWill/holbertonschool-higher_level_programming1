#!/usr/bin/python3
"""this module to instantiate
    Class:
        BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
""" Import module
"""


class Rectangle(BaseGeometry):
    """ Class definition
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
