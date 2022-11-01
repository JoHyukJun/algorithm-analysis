'''

    main.py

    Created by Jo Hyuk Jun on 2022
    Copyright © 2022 Jo Hyuk Jun. All rights reserved.

'''


def solution(lines):
    answer = 0
    
    for i in range(-100, 101):
        cnt = 0
        tmp_line = [i, i + 1]
        
        if tmp_line[0] >= lines[0][0] and tmp_line[1] <= lines[0][1]:
            cnt += 1
            
        if tmp_line[0] >= lines[1][0] and tmp_line[1] <= lines[1][1]:
            cnt += 1
            
        if tmp_line[0] >= lines[2][0] and tmp_line[1] <= lines[2][1]:
            cnt += 1
            
        if cnt > 1:
            answer += 1
            
    return answer