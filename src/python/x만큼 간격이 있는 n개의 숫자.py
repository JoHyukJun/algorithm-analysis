'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(x, n):
    if x > 0:
        return [i for i in range(x, x * n + 1, x)]
    elif x == 0:
        return [0 for i in range(n)]
    elif x < 0:
        return [i for i in range(x, x * n - 1, x)]