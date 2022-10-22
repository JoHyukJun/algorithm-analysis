'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())
answer = []

def dfs(length, eof):
    seq_set = [1, 2, 3]

    for i in range(1, length // 2 + 1):
        if answer[i * -2:-i] == answer[-i:]:
            return 

    if length == eof:
        return 0

    for i in seq_set:
        answer.append(i)
        
        if dfs(length + 1, eof) == 0:
            return 0

        answer.pop()


dfs(0, n)

print(''.join(map(str, answer)))