'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(num_list, n):
    answer = []
    hold = []
    
    for idx, val in enumerate(num_list):
        hold.append(val)
        
        if (idx + 1) % n == 0:
            answer.append(hold)
            hold = []     
        
    return answer