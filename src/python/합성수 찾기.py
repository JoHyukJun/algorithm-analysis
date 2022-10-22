'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''

            
def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        cnt = 0
        
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
                
        if cnt >= 3:
            answer += 1
    
    return answer