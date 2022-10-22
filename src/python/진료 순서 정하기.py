'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(emergency):
    answer = []
    
    sorted_emergency = sorted(emergency, reverse=True)
    
    for val in emergency:
        answer.append(sorted_emergency.index(val) + 1)
    
    return answer