'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))
n_list = sorted(n_list)
print(n_list[1])