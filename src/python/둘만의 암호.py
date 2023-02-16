'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(s, skip, index):
    answer = ''
    
    for c in s:
        tmp_idx = 1
        max_idx = index + 1
        while(True):
            asc_num = ord(c) + tmp_idx
            
            while (asc_num > 122):
                asc_num -= 26
            
            tmp_c = chr(asc_num)
            
            if (tmp_c in skip):
                tmp_idx += 1
                max_idx += 1
            else:
                tmp_idx += 1
                
            if (tmp_idx == max_idx):
                answer += tmp_c
                break
    
    return answer