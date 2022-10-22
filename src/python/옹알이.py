'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(babbling):
    answer = 0
    is_allowed_flag = False
    able_to_speak = {
        'aya': 1,
        'ye': 2,
        'woo': 3,
        'ma': 4
    }
    
    for b in babbling:
        cur_str = []
        speak_stack = []
        
        if (is_allowed_flag):
            answer += 1
        
        for c in b:
            if len(cur_str) < 4:
                cur_str.append(c)
            else:
                is_allowed_flag = False
                break
                
            tmp_check_workd = ''.join(cur_str)
                
            if tmp_check_workd in able_to_speak:
                if len(speak_stack) > 0 and speak_stack[-1] == able_to_speak[tmp_check_workd]:
                    is_allowed_flag = False
                    break
                else:
                    speak_stack.append(able_to_speak[tmp_check_workd])
                    
                cur_str = []
                    
        if len(speak_stack) > 0 and len(cur_str) == 0:
            is_allowed_flag = True
        else:
            is_allowed_flag = False
            
    if (is_allowed_flag):
        answer += 1
                
    return answer