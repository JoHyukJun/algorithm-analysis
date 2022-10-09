'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def checker(ptr_i, ptr_j, board):
    for i in range(ptr_i - 1, ptr_i + 2):
        if (i < 0 or i >= len(board)):
                continue
                
        for j in range(ptr_j - 1, ptr_j + 2):
            if (j < 0 or j >= len(board[i])):
                continue
                
            if board[i][j] != 1:
                board[i][j] = 2
                
            
def solution(board):
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                checker(i, j, board)
                
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                answer += 1
    
    return answer