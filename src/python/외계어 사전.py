'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''

            
def solution(spell, dic):
    size = len(spell)
    
    for d in dic:
        if size == len(d):
            flag = True
            for s in spell:
                if s not in d:
                    flag = False
                    
            if flag:
                return 1
    
    return 2