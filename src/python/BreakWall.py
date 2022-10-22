'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''


import sys
from collections import deque


def bfs(in_x, in_y, in_z):
    queue = deque([(in_x, in_y, in_z)])

    while queue:
        x, y, z = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if arr[nx][ny] == 1 and z == 1:
                    visited[nx][ny][z - 1] = visited[x][y][z] + 1
                    queue.append((nx, ny, z - 1))
                elif arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))

    return -1


n, m = map(int, sys.stdin.readline().rstrip().split(' '))
arr = []
answer = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][1] = 1

print(bfs(0, 0, 1))