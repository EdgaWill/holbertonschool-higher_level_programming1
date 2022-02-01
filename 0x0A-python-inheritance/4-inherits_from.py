#!/usr/bin/python3
"""the type of a object

   function:
       lookup
"""


def inherits_from(obj, a_class):
    """ function class
    """
    a = True \
        if isinstance(obj, a_class) and type(obj) is not a_class \
        else False
    return a
