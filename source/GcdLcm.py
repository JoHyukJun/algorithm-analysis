'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
import math


m, n = map(int, sys.stdin.readline().rstrip().split(' '))

print(math.gcd(m, n))
print(math.lcm(m, n))