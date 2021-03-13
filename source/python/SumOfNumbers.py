'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())

s = 0
idx = 1

while (True):
    s += idx

    if (s > n):
        idx -= 1
        break

    idx += 1

print(idx)