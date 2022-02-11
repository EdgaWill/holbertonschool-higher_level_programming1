#!/usr/bin/python3
def no_c(my_string):
    string = my_string.translate({ord(a): None for a in 'cC'})
    return string
