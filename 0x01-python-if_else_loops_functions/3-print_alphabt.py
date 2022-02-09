#!/usr/bin/python3
alphabt = 97
while(alphabt < 123):
    if 113 == alphabt or 101 == alphabt:
        alphabt += 1
        continue
    print("{:s}".format(chr(alphabt)), end='')
    alphabt += 1
