'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


t = int(sys.stdin.readline())

for _ in range(t):
    r, s = map(str, sys.stdin.readline().rstrip().split(' '))
    r = int(r)
    p = ''
    
    for i in range(len(s)):
        p = p + (s[i] * r)

    print(p)