'''

    main.py
    RemovingInPairs

    Created by Jo Hyuk Jun on 2020/05/24
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''

def solution(s):
    answer = 0

    s_list = list(s)
    stack = []
    stack.append(-1)

    for i in range(len(s_list)):
        if s_list[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s_list[i])


    if len(stack) == 1:
        answer = 1
