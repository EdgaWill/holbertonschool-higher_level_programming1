#!/usr/bin/python3
""" module for appends a string

    Functions:

"""


def append_write(filename="", text=""):
    """
       Args:

    """
    with open(filename, "a", encoding="UTF-8") as sudu:
        return sudu.write(text)
