'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys

sys.stdin = open('input.txt', 'r')


t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for test_case in range(1, t + 1):
    output = 0

    n, m, k = map(int, input().split())
    mat = [list(map(int, input().split())) + [0] * k for _ in range(n)] + [[0] * (m + k) for _ in range(k)]

    activation = ['inf'] + [[] for _ in range(10)]

    for i in range(n):
        for j in range(m):
            if mat[i][j]:
                activation[mat[i][j]].append([i, j, mat[i][j]])

    for _ in range(k):
        for life in range(10, 0, -1):
            cell = activation[life]
            forward = []
            backward = []

            for i in range(len(cell) - 1, -1, -1):
                cell[i][2] -= 1
                y, x, lp = cell[i]

                if lp == -1:
                    for j in range(4):
                        nx = (x + dx[j]) % (m + k)
                        ny = (y + dy[j]) % (n + k)

                        if not mat[ny][nx]:
                            mat[ny][nx] = life
                            forward.append([ny, nx, life])

                if lp == -life:
                    backward.append(i)


            for v in backward:
                cell.pop(v)
            cell += forward

    for i in range(1, 11):
        output += len(activation[i])

    print('#%d %d' % (test_case, output))
