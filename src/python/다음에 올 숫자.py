'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * (common[1] // common[0])