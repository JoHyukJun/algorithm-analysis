'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


def Rotate(in_key):
    m_size = len(in_key)
    tmp_mat = [[0 for _ in range(m_size)] for _ in range(m_size)]

    for i in range(m_size):
        for j in range(m_size):
            tmp_mat[j][m_size - i - 1] = in_key[i][j]

    return tmp_mat


def solution(key, lock):
    answer = False

    if len(key) > len(lock):
        return answer

    cnt = 0
    unlock = len(lock) ** 2

    for i in range(len(lock)):
        for j in range(len(lock)):
            cnt += lock[i][j]

    if cnt == unlock:
        answer = True

        return answer

    cnt = 0

    for i in range(len(key)):
        for j in range(len(key)):
            cnt += key[i][j]

    if cnt == 0:
        return answer

    base = len(lock) + ((len(key) - 1) * 2)
    mat = [[0 for _ in range(base)] for _ in range(base)]

    end_point = len(mat) - len(key) + 1

    for i in range(4):
        for j in range(end_point):
            for k in range(end_point):
                mat = [[0 for _ in range(base)] for _ in range(base)]
                cnt = 0
                is_ok = False

                for y in range(len(lock)):
                    for x in range(len(lock)):
                        mat[len(key) + y - 1][len(key) + x - 1] += lock[y][x]

                for y in range(len(key)):
                    for x in range(len(key)):
                        mat[j + y][k + x] += key[y][x]

                for y in range(len(lock)):
                    for x in range(len(lock)):
                        if mat[y + len(key) - 1][x + len(key) - 1] == 1:
                            cnt += 1

                if cnt == unlock:
                    answer = True

                    return answer

        key = Rotate(key)

    return answer
