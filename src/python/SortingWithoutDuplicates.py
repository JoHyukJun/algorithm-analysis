'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys

n = int(sys.stdin.readline())
coordinate = (list(map(int, sys.stdin.readline().rstrip().split(' '))))

coordinate = sorted(list(set(coordinate)))

for i in range(len(coordinate)):
    print(coordinate[i], end=' ')
