'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''

            
def solution(k, score):
    answer = []
    
    stack = []
    
    for s in score:
        if len(stack) == k:
            if (stack[-1] < s):
                stack.pop()
                stack.append(s)
        else:
            stack.append(s)
            
        stack = sorted(stack, reverse=True)
        answer.append(stack[-1])
    
    return answer