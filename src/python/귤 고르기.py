'''

    main.py

    Created by JO HYUK JUN on 2023
    Copyright © 2023 JO HYUK JUN. All rights reserved.

'''


def solution(k, tangerine):
    answer = 0
    
    dicter = {}
    
    for t in tangerine:
        if t in dicter:
            dicter[t] += 1
        else:
            dicter[t] = 1
            
    sorted_dicter = sorted(dicter.items(), key=lambda x: x[1], reverse=True)
    
    for s in sorted_dicter:
        answer += 1
        k -= s[1]
        
        if k <= 0:
            break
    
    return answer