'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


a, b = map(int, sys.stdin.readline().rstrip().split(' '))

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)