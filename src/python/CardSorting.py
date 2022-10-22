'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
import heapq


n = int(sys.stdin.readline())
test = []
answer = 0

for _ in range(n):
    heapq.heappush(test, int(sys.stdin.readline()))

if len(test) == 1:
    print(answer)
else:
    while (len(test) > 1):
        var1 = heapq.heappop(test)
        var2 = heapq.heappop(test)

        temp = var1 + var2
        answer += temp

        heapq.heappush(test, temp)

    print(answer)

