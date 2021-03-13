'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
import math


n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))
cnt = 0


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
    

for i in range(n):
    if (is_prime(n_list[i])):
        cnt += 1

print(cnt)
