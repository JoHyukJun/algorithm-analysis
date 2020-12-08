'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())

idx = 2

while (n > 1):
    if (n % idx == 0):
        print(idx)
        n //= idx

        continue
    else:
        idx += 1