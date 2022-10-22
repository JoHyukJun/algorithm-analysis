'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n_num = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))
n_list = sorted(n_list)

if (len(n_list) == 1):
    print(n_list[0] ** 2)
else:
    print(n_list[0] * n_list[-1])
