'''

    main.py

    Created by JO HYUK JUN on 2023
    Copyright © 2023 JO HYUK JUN. All rights reserved.

'''


def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number + 1):
        tmp_pw = 0
        
        for i in range(1, int(num ** (1 / 2)) + 1):
            if (num % i == 0):
                tmp_pw += 1
                
                if ((i ** 2) != num):
                    tmp_pw += 1
                    
        if (tmp_pw <= limit):
            answer += tmp_pw
        else:
            answer += power
    
    return answer