'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


import sys


sys.setrecursionlimit(10 ** 7)


def dfs(node):
    global answer
    
    visited[node] = True
    ckr.append(node)

    cur = n_list[node]

    if visited[cur]:
        if cur in ckr:
            answer += ckr[ckr.index(cur):]
        return
    else:
        dfs(cur)


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    n_list = [0] + list(map(int, sys.stdin.readline().rstrip().split(' ')))

    answer = []
    visited = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        if visited[i] == 0:
            ckr = []
            dfs(i)

    res = n - len(answer)

    print(res)