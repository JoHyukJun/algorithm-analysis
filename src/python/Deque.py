'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline().rstrip())

cmd = []
deque = []

for _ in range(n):
    cmd.append(list(map(str, sys.stdin.readline().rstrip().split(' '))))
    
for i in range(n):
    if (cmd[i][0] == 'push_front'):
        deque.insert(0, cmd[i][1])
    elif (cmd[i][0] == 'push_back'):
        deque.append(cmd[i][1])
    elif (cmd[i][0] == 'pop_front'):
        if (len(deque) == 0):
            print(-1)
        else:
            print(deque[0])
            deque.pop(0)
    elif (cmd[i][0] == 'pop_back'):
        if (len(deque) == 0):
            print(-1)
        else:
            print(deque[-1])
            deque.pop()
    elif (cmd[i][0] == 'size'):
        print(len(deque))
    elif (cmd[i][0] == 'empty'):
        if (len(deque) == 0):
            print(1)
        else:
            print(0)
    elif (cmd[i][0] == 'front'):
        if (len(deque) == 0):
            print(-1)
        else:
            print(deque[0])
    elif (cmd[i][0] == 'back'):
        if (len(deque) == 0):
            print(-1)
        else:
            print(deque[-1])