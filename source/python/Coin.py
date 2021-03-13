'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n, k = map(int, sys.stdin.readline().rstrip().split(' '))
n_list = []

for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

dp = [0 for _ in range(k + 1)]
dp[0] = 1

for i in range(n):
    sp = n_list[i]

    for j in range(sp, k + 1):
        dp[j] += dp[j - sp]

print(dp[k])