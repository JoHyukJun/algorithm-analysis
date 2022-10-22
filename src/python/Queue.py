'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline().rstrip())

cmd = []
queue = []

for _ in range(n):
    cmd.append(list(map(str, sys.stdin.readline().rstrip().split(' '))))
    
for i in range(n):
    if (cmd[i][0] == 'push'):
        queue.append(cmd[i][1])
    elif (cmd[i][0] == 'pop'):
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
    elif (cmd[i][0] == 'size'):
        print(len(queue))
    elif (cmd[i][0] == 'empty'):
        if (len(queue) == 0):
            print(1)
        else:
            print(0)
    elif (cmd[i][0] == 'front'):
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue[0])
    elif (cmd[i][0] == 'back'):
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue[-1])