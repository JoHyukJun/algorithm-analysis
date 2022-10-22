'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n, m = map(int, sys.stdin.readline().rstrip().split(' '))

l = []

def dfs(idx, depth):
    if depth == m:
        print(' '.join(map(str, l)))

        return

    for i in range(idx, n):
        l.append(i + 1)
        dfs(i, depth + 1)
        l.pop()

dfs(0, 0)