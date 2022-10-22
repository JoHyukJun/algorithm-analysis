'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''


import sys


def dfs(idx):
    visited[idx] = 1
    next_idx = arr[idx]
    if not visited[next_idx]:
        dfs(next_idx)


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().rstrip().split(' ')))
    visited = [0 for _ in range(n + 1)]
    visited[0] = 1

    answer = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            answer += 1

    print(answer)

