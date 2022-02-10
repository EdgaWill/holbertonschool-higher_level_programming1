#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    lenArg = len(argv)
    po = 0
    suma = 0
    if lenArg == 1:
        suma = 0
    else:
        for a in argv:
            if po != 0:
                suma += int(a)
            po += 1
    print(suma)
