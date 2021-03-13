'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


r1, s = map(int, sys.stdin.readline().rstrip().split(' '))

r2 = (s * 2) - r1
print(r2)