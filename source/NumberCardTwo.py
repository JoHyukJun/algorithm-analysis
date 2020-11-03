'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys

n = int(sys.stdin.readline())
card = dict()

temp = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for i in range(n):
    if temp[i] in card:
        card[temp[i]] += 1
    else:
        card.setdefault(temp[i], 1)

m = int(sys.stdin.readline())

ckr = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for i in range(m):
    if ckr[i] in card:
        print(card[ckr[i]], end=' ')
    else:
        print(0, end=' ')