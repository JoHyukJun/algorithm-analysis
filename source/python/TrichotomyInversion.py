'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


def solution(n):
    answer = 0
    temp = []
    
    while (True):
        if n == 0:
            break
            
        d = n % 3
        n //= 3
        temp.append(d)
        
    for i in range(len(temp)):
        mul = (3 ** (len(temp) - i - 1))
        answer += (temp[i] * mul)
    
    return answer