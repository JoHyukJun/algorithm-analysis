'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


xp = []
yp = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().rstrip().split(' '))

    if x in xp:
        xp.pop(xp.index(x))
    else:
        xp.append(x)

    if y in yp:
        yp.pop(yp.index(y))
    else:
        yp.append(y)

print('{} {}'.format(xp[0], yp[0]))