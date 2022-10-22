'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(array):
    ckr = []
    dic = {}
    
    for a in array:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
            
    max_data = max(dic.values())
            
    for key, val in dic.items():
        if val == max_data:
            ckr.append(key)
    
    return ckr[0] if len(ckr) == 1 else -1