'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

result = n * m

while (m != 0):
    temp = m % 10
    m //= 10

    print(n * temp)

print(result)