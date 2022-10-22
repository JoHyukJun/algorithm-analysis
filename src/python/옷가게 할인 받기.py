'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(price):
    if (price >= 100000 and price < 300000):
        return int(price - price * 0.05)
    elif (price >= 300000 and price < 500000):
        return int(price - price * 0.1)
    elif (price >= 500000):
        return int(price - price * 0.2)
    else:
        return price