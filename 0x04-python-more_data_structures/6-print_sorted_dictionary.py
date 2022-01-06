#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for a in sorted(a_dictionary.items()):
        print("{}: {}".format(a[0], a[1]))
