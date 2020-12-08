'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


a, i = map(int, sys.stdin.readline().rstrip().split(' '))

print((a * i) - a + 1)