'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())

q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split(' '))

    if x == 0 or y == 0:
        axis += 1
    elif x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    else:
        q4 += 1

print ('Q1: {}'.format(q1))
print ('Q2: {}'.format(q2))
print ('Q3: {}'.format(q3))
print ('Q4: {}'.format(q4))
print ('AXIS: {}'.format(axis))