#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return(None)
    for a in range(len(my_list)):
        if a == idx:
            return (my_list[a])
        return(None)
    
