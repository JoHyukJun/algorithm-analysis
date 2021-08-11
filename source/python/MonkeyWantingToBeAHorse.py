'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''


import sys
from collections import deque


def bfs():
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, z = queue.popleft()

        if x == h - 1 and y == w - 1:
            return visited[x][y][z] - 1
        
        # monkey move
        for i in range(4):
            nx = x + mm[i][0]
            ny = y + mm[i][1]


            if nx >= 0 and ny >= 0 and nx < h and ny < w and not visited[nx][ny][z] and arr[nx][ny] == 0:
                queue.append((nx, ny, z))
                visited[nx][ny][z] = visited[x][y][z] + 1
        
        # horse move
        if z < k:
            for i in range(8):
                nx = x + hm[i][0]
                ny = y + hm[i][1]

                if nx >= 0 and ny >=  0 and nx < h and ny < w and not visited[nx][ny][z + 1] and arr[nx][ny] == 0:
                    queue.append((nx, ny, z + 1))
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1

    return -1


k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().rstrip().split(' '))
arr = []

for _ in range(h):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

visited = [[[0 for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]
visited[0][0][0] = 1

mm = [(-1, 0), (1, 0), (0, 1), (0, -1)]
hm = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

print(bfs())