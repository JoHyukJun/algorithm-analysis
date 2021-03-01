'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())

for _ in range(n):
    y_score = 0
    k_score = 0

    for _ in range(9):
        y, k = map(int, sys.stdin.readline().rstrip().split(' '))

        y_score += y
        k_score += k

    if y_score > k_score:
        print('Yonsei')
    elif y_score < k_score:
        print('Korea')
    else:
        print('Draw')