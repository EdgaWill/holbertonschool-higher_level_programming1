#!/usr/bin/python3
print_comb = 0
while print_comb <= 99:
    if print_comb != 99:
        print("{:02d}, ".format(print_comb), end='')
    else:
        print("{:02d}".format(print_comb))
    print_comb += 1
