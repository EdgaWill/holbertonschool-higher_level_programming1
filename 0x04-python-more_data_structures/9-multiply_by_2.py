#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    lists = a_dictionary.items()
    new_dictionary = {}
    for tado in lists:
        new_dictionary.update({tado[0]: (tado[1] * 2)})
    return new_dictionary
