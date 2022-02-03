#!/usr/bin/python3
""" module for create an object from a JSON file
    Function:
            load_from_json_file
"""


import json
""" Import json
"""


def load_from_json_file(filename):
    """ Function definition
        Args:
    """
    with open(filename, "r") as file:
        return json.loads(file.read())
