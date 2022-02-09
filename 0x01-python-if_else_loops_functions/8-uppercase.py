#!/usr/bin/python3
def uppercase(str):
    for dat in str:
        if ord(dat) >= ord('a') and ord(dat) <= ord('z'):
            dat = chr(ord(dat) - 32)
        else:
            dat = dat
        print("{:s}".format(dat), end="")
    print('')
