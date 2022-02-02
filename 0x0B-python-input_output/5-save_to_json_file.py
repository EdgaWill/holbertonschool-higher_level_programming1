#!/usr/bin/python3
""" the module for save file
    Functions:
                save_to_json_file
"""


import json
""" Import module for to use dumps
"""


def save_to_json_file(my_obj, filename):
    """ Function definition
        Args:
             my_obj(obj): Convert to JSON for save
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
