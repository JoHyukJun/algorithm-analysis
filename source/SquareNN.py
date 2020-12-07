'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


min_val, max_val = map(int, sys.stdin.readline().rstrip().split(' '))

answer = 0
idx = 2
ckr = [0 for _ in range(1000001)]

while (idx ** 2 <= max_val):
    start = min_val // (idx ** 2)

    if (min_val % (idx ** 2) != 0):
        start += 1

    while (start * (idx ** 2) <= max_val):
        ckr[start * (idx ** 2) - min_val] = 1
        start += 1

    idx += 1

for i in range(max_val - min_val + 1):
    if (ckr[i] == 0):
        answer += 1

print(answer)