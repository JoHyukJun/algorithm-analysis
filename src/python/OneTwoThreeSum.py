'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


t = int(sys.stdin.readline())
n = []
max_n = 11

for _ in range(t):
    n.append(int(sys.stdin.readline()))

dp = [0 for _ in range(max_n + 1)]
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for i in range(len(n)):
    print(dp[n[i]])