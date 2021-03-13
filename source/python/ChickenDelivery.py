'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
from itertools import combinations


n, m = map(int, sys.stdin.readline().rstrip().split(' '))
mat = []

for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

chicken = []
home = []

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            home.append((i, j))
        elif mat[i][j] == 2:
            chicken.append((i, j))

answer = sys.maxsize

comb_list = combinations(chicken, m)
ckr = []

for cl in comb_list:
    temp = 0

    for h in home:
        min_dist = sys.maxsize

        for c in cl:
            dist = abs(h[0] - c[0]) + abs(h[1] - c[1])
            if min_dist > dist:
                min_dist = dist
        
        temp += min_dist
    
    ckr.append(temp)

answer = min(ckr)

print(answer)