'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
from itertools import combinations


output = []

while (True):
    test_case = (list(map(int, sys.stdin.readline().rstrip().split(' '))))

    if (test_case[0] == 0):
        break

    k = test_case[0]
    s = test_case[1:]

    output.append(list(combinations(s, 6)))

for i in range(len(output)):
    for j in range(len(output[i])):
        for k in range(len(output[i][j])):
            print(output[i][j][k], end=' ')
        print()
    print()
