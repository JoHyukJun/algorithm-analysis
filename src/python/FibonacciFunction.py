'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


t = int(input())

dp = [(0, 0) for _ in range(41)]
dp[0] = (1, 0)
dp[1] = (0, 1)


def fiv_counter():
    global dp
    for i in range(2, 41):
        dp[i] = (dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])

fiv_counter()

for _ in range(t):
    n = int(input())
    print(dp[n][0], dp[n][1])