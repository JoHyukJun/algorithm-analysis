'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''

            
def solution(quiz):
    answer = []
    
    for q in quiz:
        list_q = q.split(' ')
        
        if list_q[1] == '+':
            tmp = int(list_q[0]) + int(list_q[2])
            
            if tmp == int(int(list_q[4])):
                answer.append('O')
            else:
                answer.append('X')
        elif list_q[1] == '-':
            tmp = int(list_q[0]) - int(list_q[2])
            
            if tmp == int(int(list_q[4])):
                answer.append('O')
            else:
                answer.append('X')
    
    return answer