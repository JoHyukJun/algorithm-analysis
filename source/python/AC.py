'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


t = int(sys.stdin.readline())
output = []

for _ in range(t):
    p = str(sys.stdin.readline())
    n = int(sys.stdin.readline())
    pre_arr = str(sys.stdin.readline().rstrip())
    arr = []
    temp = ''
    cnt = 0

    for i in range(len(pre_arr)):
        if (pre_arr[i] == '[' or pre_arr[i] == ']' or pre_arr[i] == ','):
            if (len(temp) > 0):
                arr.append(int(temp))
                temp = ''
            else:
                continue
        else:
            temp += pre_arr[i]

    ckr = True
    is_reversed = False

    for i in range(len(p)):
        if (p[i] == 'R'):
            if (is_reversed):
                is_reversed = False
            else:
                is_reversed = True
        elif (p[i] == 'D'):
            if (len(arr) == 0):
                output.append('error')
                ckr = False
                break
            else:
                if (is_reversed):
                    arr.pop()
                else:
                    arr.pop(0)

    if (ckr):
        if (is_reversed):
            output.append(arr[::-1])
        else:
            output.append(arr)

for i in range(len(output)):
    if (output[i] == 'error'):
        print(output[i])
    else:
        print('[', end='')

        for j in range(len(output[i]) - 1):
            print(output[i][j], end='')
            print(',', end='')

        if (len(output[i]) > 0):
            print(output[i][-1], end='')
        print(']')