'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys

n = int(sys.stdin.readline())
info = [i for i in range(1, n + 1)]
stack = []
output = []

for i in range(n):
    ckr = int(sys.stdin.readline())
    flag = False

    if (len(info) > 0):
        if (ckr >= info[0]):
            while (True):
                if (ckr < info[0]):
                    break
                stack.append(info[0])
                output.append('+')
                temp = info.pop(0)
                if (ckr == temp):
                    break
    
    if (ckr >= stack[-1]):
        while (True):
            temp = stack.pop()
            output.append('-')
            if (ckr == temp):
                break
            elif (ckr > temp):
                flag = True
                break
    else:
        flag = True

    if (flag):
        output = ['NO']
        break

for i in range(len(output)):
    print(output[i])