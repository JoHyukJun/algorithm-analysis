'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


def solution(n,a,b):
    answer = 1

    front = [i + 1 for i in range(n)]
    loc = [a, b]
    loc.sort()

    while (True):
        size = n // 2
        rear = [0 for i in range(size)]
        cur = 0
        tmp = []

        for i in range(len(front)):
            if i % 2 == 1:
                tmp.append(front[i])
                if tmp == loc:
                    return answer
                elif tmp[0] in loc:
                    rear[cur] = tmp[0]
                elif tmp[1] in loc:
                    rear[cur] = tmp[1]
                cur += 1
                tmp = []
            else:
                tmp.append(front[i])

        front = rear
        answer += 1

    return answer
