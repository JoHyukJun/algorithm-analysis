'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(dots):
    for i in range(1, len(dots)):
        if dots[0][0] != dots[i][0] and dots[0][1] != dots[i][1]:
            return (abs(dots[0][0] - dots[i][0]) * abs(dots[0][1] - dots[i][1]))