'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(numbers, k):
    return numbers[(3 + (k - 2) * 2) % len(numbers) - 1]