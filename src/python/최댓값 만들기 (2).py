'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(numbers):
    sorted_num = sorted(numbers)
    
    return sorted_num[0] * sorted_num[1] if sorted_num[0] * sorted_num[1] > sorted_num[-1] * sorted_num[-2] else sorted_num[-1] * sorted_num[-2]