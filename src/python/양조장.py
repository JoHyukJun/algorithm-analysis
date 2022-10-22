'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    
    univ = ''
    point = 0

    for _ in range(n):
        u, p = map(str, sys.stdin.readline().rstrip().split(' '))

        if point < int(p):
            univ = u
            point = int(p)

    print(univ)
