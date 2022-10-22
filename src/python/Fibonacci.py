'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''


import sys

n = int(sys.stdin.readline())

arr = [0 for _ in range(n + 1)]

arr[0] = 0

if n < 1:
    print(0)

arr[1] = 1

for i in range(2, n + 1):
    arr[i] = arr[i - 1] + arr[i - 2]
    
print(arr[n])