'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(A, B):  
    case = []
    
    if A == B:
        return 0
    
    for i in range(len(A) + 1):
        tmp = A[-1]
        A = tmp + A[:-1] 
        case.append(A)
    
    return case.index(B) + 1 if B in case else -1