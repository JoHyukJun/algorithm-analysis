'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


t = int(sys.stdin.readline())
case = []

for _ in range(t):
    case.append(list(map(str, sys.stdin.readline().rstrip().split(' '))))

for i in range(len(case)):
    result = float(case[i][0])
    
    for j in range(1, len(case[i])):
        if case[i][j] == '@':
            result *= 3
        elif case[i][j] == '%':
            result += 5
        elif case[i][j] == '#':
            result -= 7

    print(format(result, '.2f'))