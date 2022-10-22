'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''

            
import math


def solution(a, b):
    flag = True
    
    gcd = math.gcd(a, b)
    b //= gcd
    
    head = 2
    
    while (True):
        if b < head:
            break
            
        if b % head == 0:
            b //= head
            if head != 2 and head != 5:
                flag = False
                break
        else:
            head += 1
    
    return 1 if flag else 2