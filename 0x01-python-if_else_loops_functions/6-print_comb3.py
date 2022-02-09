#!/usr/bin/python3
comb1 = 0
comb2 = 1
while comb1 <= 8:
    while comb2 <= 9:
        if comb1 != comb2:
            print("{:d}".format(comb1), end='')
            if comb1 != 8:
                print("{:d}, ".format(comb2), end='')
            else:
                print("{:d}".format(comb2))
        comb2 += 1
    comb2 = comb1 + 1
    comb1 += 1
