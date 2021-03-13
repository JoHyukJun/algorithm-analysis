'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


mat = []
axis = []
sema = False

for _ in range(9):
    mat.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 0:
            axis.append((i, j))


def col(ptr, cidx):
    for i in range(len(mat)):
        if ptr == mat[i][cidx]:
            return False

    return True


def row(ptr, ridx):
    if ptr in mat[ridx]:
        return False

    return True


def sqr(ptr, ridx, cidx):
    r = (ridx // 3) * 3
    c = (cidx // 3) * 3
     
    for i in range(3):
        for j in range(3):
            if ptr == mat[i + r][j + c]:
                return False

    return True


def dfs(ptr):
    global sema

    if sema:
        return
    
    if ptr == len(axis):
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                print(mat[i][j], end=' ')
            print()
        
        sema = True
        return

    for i in range(1, 10):
        x = axis[ptr][0]
        y = axis[ptr][1]

        if row(i, x) and col(i, y) and sqr(i, x, y):
            mat[x][y] = i
            dfs(ptr + 1)
            mat[x][y] = 0
            
dfs(0)