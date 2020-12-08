'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


k, n, m = map(int, sys.stdin.readline().rstrip().split(' '))

if k * n < m:
    print(0)
else:
    print(k * n - m)