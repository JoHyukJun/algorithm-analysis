'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(n, t):
    answer = n
    
    for i in range(t):
        answer = answer * 2
        
    return answer