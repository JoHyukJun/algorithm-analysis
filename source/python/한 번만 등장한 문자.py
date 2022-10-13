'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''

            
def solution(s):
    answer = ''
    dic = {}
    
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
            
    for key, val in dic.items():
        if val == 1:
            answer += key
            
    answer = ''.join(sorted(answer))
        
    return answer