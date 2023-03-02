'''

    main.py

    Created by JO HYUK JUN on 2023
    Copyright © 2023 JO HYUK JUN. All rights reserved.

'''


def solution(cards1, cards2, goal):
    answer = ''
    flag = True
    
    for g in goal:
        if (len(cards1) > 0 and g == cards1[0]):
            cards1.pop(0)
        elif (len(cards2) > 0 and g == cards2[0]):
            cards2.pop(0)
        else:
            flag = False
            break
            
    if (flag):
        answer = 'Yes'
    else:
        answer = 'No'
    
    return answer