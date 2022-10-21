'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x - n), -x))