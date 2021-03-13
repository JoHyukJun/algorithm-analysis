'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


t = int(sys.stdin.readline())

for _ in range(t):
    quiz = str(sys.stdin.readline().rstrip())
    
    score = 0 
    point = 1

    for i in range(len(quiz)):
        if quiz[i] == 'O':
            if i > 0 and quiz[i] == quiz[i - 1]:
                point += 1
                score += point
            else:
                point = 1
                score += point

    print(score)