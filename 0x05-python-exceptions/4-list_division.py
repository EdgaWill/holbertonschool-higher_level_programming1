#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_lista3 = []
    for a in range(list_length):
        try:
            item = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            item = 0
        except ZeroDivisionError:
            print("division by 0")
            item = 0
        except IndexError:
            print("out of range")
            item = 0
        finally:
            my_lista3.append(item)
    return (my_lista3)
