'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


import sys


n, k = map(int, sys.stdin.readline().rstrip().split(' '))

answer = 0
coin = []

for _ in range(n):
    coin.append(int(sys.stdin.readline()))

coin = coin[::-1]

for c in coin:
    if c > k:
        continue
    else:
        answer += k // c
        k = k % c

print(answer)