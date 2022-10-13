'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


def solution(n):
    idx = 1
    facto = [1]
    
    
    while (True):
        if facto[-1] > n:
            return idx - 1
        
        idx += 1
        facto.append(facto[-1] * idx)