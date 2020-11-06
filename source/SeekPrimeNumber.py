'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
import math


def is_prime(number):
    number = abs(int(number))

    if (number == 1):
        return False

    if (number == 2):
        return True

    if (number % 2 == 0):
        return False

    sq_number = math.sqrt(number)
    basis = 3

    while sq_number >= basis:
        if (number % basis == 0):
            return False
        basis += 2

    return True


m, n = map(int, sys.stdin.readline().rstrip().split(' '))

for i in range(m, n + 1):
    if (is_prime(i)):
        print(i)