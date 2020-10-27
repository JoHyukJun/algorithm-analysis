'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


def solution(n):
    answer = []
    
    tri = [[0 for _ in range(n)] for _ in range(n)]
    
    x, y = -1, 0
    in_num = 1
    
    for i in range(n):
        for j in range(i, len(tri[i])):
            if (i % 3 == 0):
                x += 1
            elif (i % 3 == 1):
                y += 1
            elif (i % 3 == 2):
                x -= 1
                y -= 1
            
            tri[x][y] = in_num
            in_num += 1
    
    temp = []
    
    for i in range(n):
        temp.extend(tri[i])
        
    for i in range(len(temp)):
        if (temp[i] == 0):
            continue
        else:
            answer.append(temp[i])
    
    return answer