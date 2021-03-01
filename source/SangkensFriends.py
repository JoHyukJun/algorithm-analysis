'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


while (True):
    m, f = map(int, sys.stdin.readline().rstrip().split(' '))
    
    if m == 0 and f == 0:
        break

    print(m + f)