'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
from collections import Counter

n = int(sys.stdin.readline())
score = []

for _ in range(n):
    dices = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    ckr = Counter(dices)

    result = ckr.most_common(1)[0]

    if result[1] == 1:
        score.append(max(dices) * 100)
    elif result[1] == 2:
        score.append(1000 + result[0] * 100)
    else:
        score.append(10000 + result[0] * 1000)

print(max(score))