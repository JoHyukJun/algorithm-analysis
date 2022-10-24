'''

    main.py

    Created by Jo Hyuk Jun on 2022
    Copyright © 2022 Jo Hyuk Jun. All rights reserved.

'''


def solution(score):
    answer = [0 for i in range(len(score))]
    rank = {}
    
    for idx, s in enumerate(score):
        tot = s[0] + s[1] 
        
        if tot in rank:
            rank[tot] += 1
        else:
            rank[tot] = 1
            
    rank = sorted(rank.items(), reverse=True)
    cur_rank = 1
    
    for i in range(len(rank)):
        for j in range(len(score)):
            tot = score[j][0] + score[j][1]
            
            if rank[i][0] == tot:
                answer[j] += cur_rank
                
        cur_rank += rank[i][1]
                
    return answer
