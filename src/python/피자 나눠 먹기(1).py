'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(n):
    if (n <= 7):
        return 1
    else:
        if n % 7 == 0:
            return n // 7
        else:
            return n // 7 + 1