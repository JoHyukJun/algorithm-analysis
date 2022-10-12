'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(num, k):
    for idx, val in enumerate(str(num)):
        if int(val) == k:
            return idx + 1
        
    return -1