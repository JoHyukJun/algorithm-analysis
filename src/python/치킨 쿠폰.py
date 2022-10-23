'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(chicken):
    answer = 0
    
    while (True):
        answer += (chicken // 10)
        chicken = chicken // 10 + chicken % 10
        
        if chicken < 10:
            break
    
    return answer