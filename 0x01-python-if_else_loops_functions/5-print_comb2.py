#!/usr/bin/python3
comb = 0
while comb <= 99:
    if comb != 99:
        print("{:02d}, ".format(comb), end='')
    else:
        print("{:02d}".format(comb))
    comb += 1
