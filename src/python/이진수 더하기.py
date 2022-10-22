'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''

            
def solution(bin1, bin2):
    answer = ''
    adder = 0
    
    res_bin = int(bin1) + int(bin2)
    res_bin = str(res_bin)
    
    for b in res_bin[::-1]:
        if int(b) + adder == 0:
            answer += '0'
            adder = 0
            continue
        elif int(b) + adder == 1:
            answer += '1'
            adder = 0
            continue
        elif int(b) + adder == 2:
            answer += '0'
            adder = 1
            continue
        elif int(b) + adder == 3:
            answer += '1'
            adder = 1
            continue
            
    if adder == 1:
        answer += '1'
        
    answer = answer[::-1]
    
    return answer