'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())
rope = []
answer = 0

for _ in range(n):
    rope.append(int(sys.stdin.readline()))

rope.sort()

for r in rope:
    if answer < n * r:
        answer = n * r
    n -= 1

print(answer)