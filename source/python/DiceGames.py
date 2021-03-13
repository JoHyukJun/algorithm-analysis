'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())

a_score = 100
b_score = 100

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))

    if a > b:
        b_score -= a
    elif a < b:
        a_score -= b

print(a_score)
print(b_score)