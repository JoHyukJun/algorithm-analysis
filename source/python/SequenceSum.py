'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))

answer = n_list[0]

dp = [0 for _ in range(n)]
dp[0] = n_list[0]

for i in range(1, len(dp)):
    temp = dp[i - 1] + n_list[i]

    if temp > n_list[i]:
        dp[i] = temp
    else:
        dp[i] = n_list[i]

    if answer < dp[i]:
        answer = dp[i]


print(answer)