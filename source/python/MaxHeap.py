'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
import heapq


n = int(sys.stdin.readline())
test = []

for _ in range(n):
    x = int(sys.stdin.readline())
    x *= -1

    if x == 0:
        if len(test) == 0:
            print(0)
        else:
            print(test[0] * -1)
            heapq.heappop(test)
    else:
        heapq.heappush(test, x)