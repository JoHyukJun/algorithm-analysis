'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


test_case = int(sys.stdin.readline())
output = []

for _ in range(test_case):
    n, m = map(int, sys.stdin.readline().rstrip().split(' '))
    priority = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    waiting = []

    for i in range(len(priority)):
        waiting.append([i, priority[i]])

    cnt = 0
    while (True):
        max_pl = max(waiting, key=lambda x:x[1])
        max_p = max_pl[1]
        printing = []

        if (waiting[0][1] >= max_p):
            printing = waiting.pop(0)
            cnt += 1
        else:
            temp = waiting.pop(0)
            waiting.append(temp)
        
        if (len(printing) != 0):
            if (printing[0] == m):
                output.append(cnt)
                break

for i in range(len(output)):
    print(output[i])