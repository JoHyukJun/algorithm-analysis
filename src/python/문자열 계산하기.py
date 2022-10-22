'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(my_string):
    answer = 0
    arr = my_string.split(' ')
    
    answer = int(arr[0])
    flag = True
    
    for i in range(1, len(arr)):
        if arr[i] == '+':
            flag = True
        elif arr[i] == '-':
            flag = False
        else:
            if flag:
                answer += int(arr[i])
            else:
                answer -= int(arr[i])
    
    return answer