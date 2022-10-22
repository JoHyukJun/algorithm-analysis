'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(n):
    if (n % 6 == 0):
        return n // 6
    else:
        m = n
        while (True):
            if (m % 6 == 0):
                return m // 6
            else:
                m += n