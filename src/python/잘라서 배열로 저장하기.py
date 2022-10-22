'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''

            
def solution(my_str, n):
    answer = []
    tmp = ''
    
    for idx, val in enumerate(my_str):
        tmp += val
        
        if (idx + 1) % n == 0:
            answer.append(tmp)
            tmp = ''
            
    if tmp:
        answer.append(tmp)
    
    return answer