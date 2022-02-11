#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) - 1 < idx:
        return my_list
    new_list = list(my_list)
    for a in range(len(my_list)):
        if idx != a:
            new_list[a] = my_list[a]
        else:
            new_list[a] = element
    return new_list
