'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


answer = [0, 0]

def comp(x, y, in_arr, f_size, in_visited):
    global answer
    
    output = -1
    ff_size = f_size // 2
    
    if (f_size == 1 or in_visited[x][y] != -1):
        return output
    
    holder = in_arr[x][y]
    ckr = True
    
    for i in range(x, x + f_size):
        for j in range(y, y + f_size):
            if (i == 0 and j == 0):
                continue
            
            if (in_arr[i][j] != holder):
                ckr = False
                break
        if (not ckr):
            break
        
    if (ckr):
        answer[holder] += 1
        
        for i in range(x, x + f_size):
            for j in range(y, y + f_size):
                in_visited[i][j] = holder
                
        output = holder
        return output
                
    comp(x, y, in_arr, ff_size, in_visited)
    comp(x, y + ff_size, in_arr, ff_size, in_visited)
    comp(x + ff_size, y, in_arr, ff_size, in_visited)
    comp(x + ff_size, y + ff_size, in_arr, ff_size, in_visited)

    return output


def solution(arr):
    global answer
    
    arr_size = len(arr)
    filter_size = arr_size
    
    visited = [[-1 for _ in range(arr_size)] for _ in range(arr_size)]
    
    comp(0, 0, arr, filter_size, visited)

    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if (visited[i][j] == -1):
                answer[arr[i][j]] += 1
    
    return answer