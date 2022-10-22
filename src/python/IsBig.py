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
        print('Yes')
    else:
        print('No')