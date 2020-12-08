'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())

cute = 0
not_cute = 0

for _ in range(n):
    op = int(sys.stdin.readline())

    if op == 1:
        cute += 1
    else:
        not_cute += 1

if cute > not_cute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')