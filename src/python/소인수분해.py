'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(n):
    answer = []
    head = 2
    
    while (True):
        if n < head:
            break
            
        if n % head == 0:
            n //= head
            if head not in answer:
                answer.append(head)
        else:
            head += 1
            
    return answer