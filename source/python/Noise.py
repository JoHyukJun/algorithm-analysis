'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


a = str(sys.stdin.readline().rstrip())
operation = str(sys.stdin.readline().rstrip())
b = str(sys.stdin.readline().rstrip())

if operation == '*':
    z_cnt = len(a) + len(b) - 2
    print('1' + ('0' * z_cnt))
elif operation == '+':
    if len(a) == len(b):
        print('2' + ('0' * (len(a) - 1)))
    else:
        print('1' + ('0' * (abs(len(a) - len(b)) - 1)) + '1' + ('0' * (min(len(a), len(b)) - 1)))