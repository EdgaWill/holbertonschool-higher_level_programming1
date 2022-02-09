#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    dat = number % 10
    print('{:d}'.format(dat), end='')
    return (dat)
