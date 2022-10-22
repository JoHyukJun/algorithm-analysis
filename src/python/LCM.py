'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
import math


t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))

    print((a * b) // math.gcd(a, b))