'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(id_pw, db):
    for val in db:
        if id_pw[0] == val[0]:
            if id_pw[1] == val[1]:
                return 'login'
            else:
                return 'wrong pw'

    return 'fail'