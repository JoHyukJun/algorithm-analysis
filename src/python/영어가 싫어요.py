'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(numbers):
    answer = ''
    
    dic = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    num = ''
    
    for n in numbers:
        if num in dic:
            answer += str(dic[num])
            num = ''
            
        num += n
            
    answer += str(dic[num])
    
    return int(answer)