'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(array, n):
    answer = 0
    ckr = 101
    
    for idx, val in enumerate(array):
        if ckr > abs(val - n):
            ckr = abs(val - n)
            answer = val
        elif ckr == abs(val - n):
            if answer > val:
                answer = val
        
    return answer