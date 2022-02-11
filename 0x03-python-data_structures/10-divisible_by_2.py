#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lista = list(my_list)
    for a in range(len(my_list)):
        if my_list[a] % 2 == 0:
            lista[a] = True
        else:
            lista[a] = False
    return lista
