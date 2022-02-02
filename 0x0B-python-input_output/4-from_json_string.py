#!/usr/bin/python3
""" the module for represented a JSON
    Function:
        from_json_string
"""


import json
""" Import json module for converto json
"""


def from_json_string(my_str):
    """ Function definition
        Args:
            convert to object
"""
    return json.loads(my_str)
