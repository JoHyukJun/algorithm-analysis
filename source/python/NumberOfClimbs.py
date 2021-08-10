'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())

dp = [[0 for _ in range(10)] for _ in range(1001)]
dp[0] = [1 for _ in range(101)]

for i in range(1, n + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] = dp[i][j] + dp[i - 1][k]

print(dp[n][9] % 10007)