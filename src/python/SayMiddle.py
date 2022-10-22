'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
import heapq


n = int(sys.stdin.readline())
max_heap = []
min_heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-x, x))
    else:
        heapq.heappush(min_heap, (x, x))

    if len(min_heap) > 0 and max_heap[0][1] > min_heap[0][1]:
        tmp1 = heapq.heappop(max_heap)[1]
        tmp2 = heapq.heappop(min_heap)[1]

        heapq.heappush(max_heap, (-tmp2, tmp2))
        heapq.heappush(min_heap, (tmp1, tmp1))

    print(max_heap[0][1])