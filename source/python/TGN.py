'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())

for _ in range(n):
    r, e, c = map(int, sys.stdin.readline().rstrip().split(' '))

    if r < e - c:
        print('advertise')
    elif r == e - c:
        print('does not matter')
    else:
        print('do not advertise')