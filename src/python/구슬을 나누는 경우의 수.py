'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


import math


def solution(balls, share):
    return (math.factorial(balls) // (math.factorial(balls - share) * math.factorial(share)))