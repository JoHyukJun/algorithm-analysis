'''

    main.py
    Ending

    Created by Jo Hyuk Jun on 2020/05/24
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''

def solution(n, words):
    answer = []

    ckr = []
    ckr.append(words[0])

    for i in range(1, len(words)):
        user = i % n
        num = i // n

        if words[i][0] != words[i - 1][-1]:
            answer.append(user + 1)
            answer.append(num + 1)

            return answer

        if words[i] in ckr:
            answer.append(user + 1)
            answer.append(num + 1)

            return answer
        else:
            ckr.append(words[i])


    answer.append(0)
    answer.append(0)

    return answer
