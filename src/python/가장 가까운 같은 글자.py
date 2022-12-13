'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''

            
def solution(s):
    answer = []
    
    s = list(s)
    
    for idx, val in enumerate(s):
        if idx == 0:
            answer.append(-1)
            continue
        
        tmp = s[:idx]
        tmp = tmp[::-1]
        flag = False
        
        for iidx, vval in enumerate(tmp):
            if (val == vval):
                answer.append(iidx + 1)
                flag = True
                break
                
        if (not flag):
            answer.append(-1)
                
    return answer