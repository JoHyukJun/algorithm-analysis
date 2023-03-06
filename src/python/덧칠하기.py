'''

    main.py

    Created by JO HYUK JUN on 2023
    Copyright © 2023 JO HYUK JUN. All rights reserved.

'''


def solution(n, m, section):
    answer = 0
    
    wall = [1 for _ in range(n)]
    
    for s in section:
        wall[s - 1] = 0
        
    for i in range(len(wall)):
        if wall[i] == 0:
            answer += 1

            for j in range(m):
                if (i + j) >= len(wall):
                    break
                else:
                    wall[i + j] = 1
    
    return answer