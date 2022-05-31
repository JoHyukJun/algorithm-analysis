'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    queue.append((0, 0))

    visited[0][0] = 1

    res = 0

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if n > nx >= 0 and k > ny >= 0 and visited[nx][ny] == 0:
                if cheeze[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif cheeze[nx][ny] == 1:
                    res += 1
                    cheeze[nx][ny] = 0
                    visited[nx][ny] = 1

    answer.append(res)

    return res


n, k = map(int, sys.stdin.readline().rstrip().split(' '))
cheeze = []

in_time = 0
answer = []

for _ in range(n):
    cheeze.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

while True:
    visited = [[0 for _ in range(k)] for _ in range(n)]

    ckr = bfs()
    in_time += 1

    if ckr == 0:
        break

print(in_time - 1)
print(answer[-2])