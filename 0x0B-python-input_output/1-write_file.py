#!/usr/bin/python3
"""write in a file

   Functions:
        file
"""


def write_file(filename="", text=""):
    """ Function
        Args:
    """
    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)
