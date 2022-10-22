'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(my_string):
    answer = 0
    
    num = ''
    
    for c in my_string:
        if c.isdecimal():
            num += c
        else:
            if len(num) == 0:
                continue
            answer += int(num)
            num = ''
            
    if len(num) != 0:
        answer += int(num)
    
    return answer