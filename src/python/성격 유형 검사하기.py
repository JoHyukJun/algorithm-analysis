'''

    main.py

    Created by Jo Hyuk Jun on 2022
    Copyright © 2022 Jo Hyuk Jun. All rights reserved.

'''


def solution(survey, choices):
    answer = ''
    
    dic = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    
    for idx, val in enumerate(survey):
        conf = choices[idx]
        
        if conf < 4:
            dic[val[0]] += (4 - conf)
        elif conf > 4:
            dic[val[1]] += (conf - 4)
                
    if dic['R'] > dic['T']:
        answer += 'R'
    elif dic['R'] < dic['T']:
        answer += 'T'
    else:
        answer += 'R'
        
    if dic['C'] > dic['F']:
        answer += 'C'
    elif dic['C'] < dic['F']:
        answer += 'F'
    else:
        answer += 'C'
        
    if dic['J'] > dic['M']:
        answer += 'J'
    elif dic['J'] < dic['M']:
        answer += 'M'
    else:
        answer += 'J'
        
    if dic['A'] > dic['N']:
        answer += 'A'
    elif dic['A'] < dic['N']:
        answer += 'N'
    else:
        answer += 'A'
                
    return answer