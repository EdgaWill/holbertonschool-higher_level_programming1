#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    for a in range (len(my_list)):
        if a == idx:
            my_list[a] = element
            break
        return (my_list)
