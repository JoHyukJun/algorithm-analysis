'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
from itertools import combinations


n, s = map(int, sys.stdin.readline().rstrip().split(' '))
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))

f_arr = []
cnt = 0

for i in range(1, len(arr) + 1):
    f_arr.append(list(combinations(arr, i)))

for i in range(len(f_arr)):
    for j in range(len(f_arr[i])):
        if sum(f_arr[i][j]) == s:
            cnt += 1

print(cnt)