'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


MAX = 1000001

n = int(input())

dp = [0 for _ in range(MAX)]
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= 15746

print(dp[n]))