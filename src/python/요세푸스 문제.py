'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys

n, k = map(int, sys.stdin.readline().rstrip().split(' '))

arr = [i for i in range(1, n + 1)]
cur_idx = 0
output = []

for i in range(n):
    arr_size = len(arr)
    del_idx = (cur_idx + k - 1) % arr_size
    output.append(arr[del_idx])
    arr.pop(del_idx)
    cur_idx = del_idx

print('<', end='')
for i in range(len(output) - 1):
    print(output[i], end=', ')
print(output[-1], end='')
print('>')