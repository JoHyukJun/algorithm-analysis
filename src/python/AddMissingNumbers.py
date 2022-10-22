'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(numbers):
    answer = 0
    
    sorted_numbers = sorted(numbers)
    idx = 0
    max_idx = len(sorted_numbers)
    
    for i in range(10):
        if i == sorted_numbers[idx]:
            if idx == max_idx - 1:
                continue
            idx += 1
        else:
            answer += i
    
    return answer