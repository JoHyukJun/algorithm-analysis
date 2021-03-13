'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


t = int(sys.stdin.readline())

a = 300
b = 60
c = 10

a_cnt = 0
b_cnt = 0
c_cnt = 0

while (True):
    if t == 0:
        print('{} {} {}'.format(a_cnt, b_cnt, c_cnt))
        break

    if t - a >= 0:
        t -= a
        a_cnt += 1
        continue
    elif t - b >= 0:
        t -= b
        b_cnt += 1
        continue
    elif t - c >= 0:
        t -= c
        c_cnt += 1
        continue
    else:
        print(-1)
        break
