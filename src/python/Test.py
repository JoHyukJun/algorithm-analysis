'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''

def solution(n, quests):
    answer = []
    
    q_dict = dict()
    
    for q in quests:
        if q[0] not in q_dict.keys():
            q_dict[q[0]] = [q[1]]
        else:
            q_dict[q[0]].append(q[1])
        
    print(q_dict)
    
    for k in q_dict.values():
        print(k)

    return answer


n = 5
qest = 	[[1,3],[1,4],[3,5],[5,4]]

print(solution(n, qest))