#!/usr/bin/python3
print_comb2 = 0
while print_comb2 <= 99:
    if print_comb2 != 99:
        print("{:02d}, ".format(print_comb2), end='')
    else:
        print("{:02d}".format(print_comb2))
    print_comb2 += 1
