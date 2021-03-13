'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


def solution(arr):
    answer = []
    
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if (arr[i] == arr[i - 1]):
            continue
        else:
            answer.append(arr[i])
    
    return answer