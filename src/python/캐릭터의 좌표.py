'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(keyinput, board):
    answer = [0, 0]
    
    x_limit = (board[0] - 1) // 2
    y_limit = (board[1] - 1) // 2
    
    for k in keyinput:
        if k == 'left':
            if answer[0] - 1 <= -x_limit:
                answer[0] = -x_limit
            else:
                answer[0] -= 1
        elif k == 'right':
            if answer[0] + 1 >= x_limit:
                answer[0] = x_limit
            else:
                answer[0] += 1
        elif k == 'up':
            if answer[1] + 1 >= y_limit:
                answer[1] = y_limit
            else:
                answer[1] += 1
        elif k == 'down':
            if answer[1] - 1 <= -y_limit:
                answer[1] = -y_limit
            else:
                answer[1] -= 1

    return answer