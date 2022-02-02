#!/usr/bin/python3
"""read of a file

    Function:
        File
"""


def read_file(filename=""):
    """Funtion

       Args:
           filename
    """
    with open(filename, "r", encoding="UTF-8") as runu:
        print(runu.read(), end="")
