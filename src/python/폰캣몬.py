'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(nums):
    answer = 0
    
    sel_num = len(nums) // 2
    
    nums = list(set(nums))
    
    if len(nums) > sel_num:
        answer = sel_num
    else:
        answer = len(nums)
    
    return answer