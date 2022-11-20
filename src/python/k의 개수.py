'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(i, j, k):
    answer = 0
    
    for num in range(i, j + 1):
        for c in str(num):
            if c == str(k):
                answer += 1
    
    return answer