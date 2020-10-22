'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


n = int(input())

dp = [0 for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    
print(dp[n])