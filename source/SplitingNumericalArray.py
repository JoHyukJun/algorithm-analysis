'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


def solution(arr, divisor):
    answer = []
    
    for i in range(len(arr)):
        if (arr[i] % divisor == 0 and arr[i] // divisor > 0):
            answer.append(arr[i])
    
    if (len(answer) == 0):
        answer.append(-1)
        
    answer = sorted(answer)
    
    return answer