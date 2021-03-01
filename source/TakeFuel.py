'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''


import sys
import heapq

n = int(sys.stdin.readline())
hq = []

for _ in range(n):
    heapq.heappush(hq, list(map(int, sys.stdin.readline().rstrip().split(' '))))

l, p = map(int, sys.stdin.readline().rstrip().split(' '))

cur = []
cnt = 0

if l <= p:
    print(0)
else:
    while l > p:
        while hq and hq[0][0] <= p:
            t1, t2 = heapq.heappop(hq)
            heapq.heappush(cur, [t2 * -1, t1])

        if not cur:
            cnt -= 1
            break

        t2, t1 = heapq.heappop(cur)
        p += t2 * -1
        cnt += 1

    print(cnt)