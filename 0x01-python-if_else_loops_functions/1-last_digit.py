#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    date = number % 10
else:
    date = -number % 10
    date = -date

if date == 0:
    print('Last digit of {:d} is 0 and is 0'.format(number))
elif date < 6:
    print('Last digit of {:d} is {:d} and is less than 6 and not \
0'.format(number, date))
else:
    print('Last digit of {:d} is {:d} and is greater than 5\
'.format(number, date))
