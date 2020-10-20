'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
import copy

sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(in_mat, idx):
    flag = update_output(in_mat, idx)

    if flag:
        return

    for y in range(w):
        ckr = 0

        for x in range(h):
            if not in_mat[x][y]:
                continue

            else:
                prev_mat = copy.deepcopy(in_mat)
                queue = [(x, y, in_mat[x][y])]

                bfs(in_mat, queue)

                out_mat = [[0 for _ in range(w)] for _ in range(h)]

                remover(in_mat, out_mat)

                ckr = 1

            if ckr == 1:
                dfs(out_mat, idx + 1)
                in_mat = prev_mat
                break

    dfs(in_mat, n)


def update_output(in_mat, idx):
    global output

    if idx == n:
        cnt = 0

        for i in range(h):
            cnt += in_mat[i].count(0)

        res = w * h - cnt

        if res < output:
            output = res

        return True
    else:
        return False


def bfs(in_mat, queue):
    while queue:
        t = queue.pop(0)

        if t[2] == 1:
            in_mat[t[0]][t[1]] = 0
        else:
            in_mat[t[0]][t[1]] = 0

            for i in range(1, t[2]):
                for j in range(4):
                    if h > t[0] + dx[j] * i >= 0 and w > t[1] + dy[j] * i >= 0 and in_mat[t[0] + dx[j] * i][t[1] + dy[j] * i] != 0:
                        if (t[0] + dx[j] * i, t[1] + dy[j] * i, in_mat[t[0] + dx[j] * i][t[1] + dy[j] * i]) not in queue:
                            queue.append((t[0] + dx[j] * i, t[1] + dy[j] * i, in_mat[t[0] + dx[j] * i][t[1] + dy[j] * i]))

    return


def remover(in_mat, out_mat):
    for i in range(w):
        tmp = []

        for j in range(h):
            if in_mat[j][i]:
                tmp.append(in_mat[j][i])

        for k in range(len(tmp)):
            out_mat[h - len(tmp) + k][i] = tmp[k]

    return


for test_case in range(1, T + 1):
    output = 999999999

    n, w, h = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(h)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    dfs(mat, 0)

    print('#%d %d' % (test_case, output))
