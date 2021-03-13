'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


while (True):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))

    if a == 0 and b == 0:
        break

    if a > b:
        if a % b == 0:
            print('multiple')
        else:
            print('neither')
    else:
        if b % a == 0:
            print('factor')
        else:
            print('neither')