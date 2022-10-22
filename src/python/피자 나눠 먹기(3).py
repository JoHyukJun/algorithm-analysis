'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(slice, n):
    if (n // slice == 0):
        return 1
    elif (n // slice > 0):
        if (n % slice == 0):
            return n // slice
        else:
            return n // slice + 1