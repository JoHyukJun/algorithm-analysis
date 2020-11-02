'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys

n = int(sys.stdin.readline())
coordinate = []

for _ in range(n):
    coordinate.append(tuple(map(int, sys.stdin.readline().rstrip().split(' '))))

coordinate = sorted(coordinate, key=lambda coordinate:(coordinate[1], coordinate[0]))

for i in range(len(coordinate)):
    print(coordinate[i][0], coordinate[i][1])