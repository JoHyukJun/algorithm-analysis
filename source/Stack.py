'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys

n = int(sys.stdin.readline())
stack = []
cmd = []

for _ in range(n):
    cmd.append(list(map(str, sys.stdin.readline().rstrip().split(' '))))

for i in range(n):
    if (cmd[i][0] == 'push'):
        stack.append(cmd[i][1])
    elif (cmd[i][0] == 'pop'):
        if (len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif (cmd[i][0] == 'size'):
        print(len(stack))
    elif (cmd[i][0] == 'empty'):
        if (len(stack) == 0):
            print(1)
        else:
            print(0)
    else:
        if (len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
