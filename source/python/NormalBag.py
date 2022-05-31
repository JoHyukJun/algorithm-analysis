'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''


import sys


n, k = map(int, sys.stdin.readline().rstrip().split(' '))

knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

obj = [[0, 0]]

for _ in range(n):
    obj.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = obj[i][0]
        v = obj[i][1]

        if w > j:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(knapsack[i - 1][j - w] + v, knapsack[i - 1][j])

print(knapsack[n][k])