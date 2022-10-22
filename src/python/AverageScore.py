'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


score_sum = 0

for _ in range(5):
    score = int(sys.stdin.readline())

    if score < 40:
        score = 40

    score_sum += score

print(score_sum // 5)