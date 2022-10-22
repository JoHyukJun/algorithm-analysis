'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''

            
def solution(clothes):
    answer = 1
    
    dic = dict()
    
    for i in range(len(clothes)):
        if clothes[i][1] in dic:
            dic[clothes[i][1]] += 1
        else:
            dic[clothes[i][1]] = 1
    
    for val in dic.values():
        answer *= (val + 1)
    
    answer -= 1
    
    return answer