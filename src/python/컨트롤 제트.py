'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(s):
    stack = []
    
    s = s.split(' ')
    
    for c in s:
        if c == 'Z':
            if len(stack) > 0:
                stack.pop()
            else:
                continue
        else:
            stack.append(int(c))
    
    return sum(stack)