'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(num, total):
    head = total - num + 100
    tail = total + 100
    
    num_list = [i for i in range(head, tail)]
    
    tmp_sum = sum(num_list)
    cnt = 0
    
    while (True):
        if tmp_sum == total:
            for i in range(len(num_list)):
                num_list[i] -= cnt
                
            return num_list
        
        tmp_sum -= num
        cnt += 1