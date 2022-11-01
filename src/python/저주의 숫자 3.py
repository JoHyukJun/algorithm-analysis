'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(n):
    list = [i for i in range(1, 300) if (i % 3 != 0 and str(i).find('3') == -1)]

    return list[n - 1]