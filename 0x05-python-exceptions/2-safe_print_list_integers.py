#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    sig = 0
    count = 0
    while sig < x:
        try:
            if type(my_list[sig]) is int:
                print("{:d}".format(my_list[sig]), end="")
                count += 1
        except IndexError:
            raise
        sig += 1
    print()
    return count
