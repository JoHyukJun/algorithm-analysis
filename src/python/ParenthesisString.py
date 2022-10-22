'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys

n = int(sys.stdin.readline())
parenthesis = []
output = []

for _ in range(n):
    parenthesis.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(n):
    stack = []
    ckr = True
    for j in range(len(parenthesis[i])):
        if (parenthesis[i][j] == '('):
            stack.append(1)
        else:
            if (len(stack) == 0):
                ckr = False
                break
            else:
                stack.pop()

    if (len(stack) != 0):
        ckr = False

    if (ckr):
        output.append('YES')
    else:
        output.append('NO')

for i in range(len(output)):
    print(output[i])