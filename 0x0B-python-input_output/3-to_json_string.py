#!/usr/bin/python3
""" Use the module for return the JSON representation
    Functions:
           to_json_string
"""


import json
""" Import module json
"""


def to_json_string(my_obj):
    """ Function definition
        Args:
        my_obj : object to json
    """
    return json.dumps(my_obj)
