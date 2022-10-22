'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


from itertools import permutations


def solution(numbers):
    answer = []
    
    temp_list = list(permutations(numbers, 2))
    
    for i in range(len(temp_list)):
        temp_list[i] = sum(temp_list[i])
        
    answer = sorted(list(set(temp_list)))
    
    return answer