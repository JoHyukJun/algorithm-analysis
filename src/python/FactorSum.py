'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


while (True):
    n = int(sys.stdin.readline())

    if n == -1:
        break
    
    factor = []
    div = 1

    while (div < n):
        if n % div == 0:
            factor.append(div)

        div += 1
    
    if sum(factor) == n:
        print('{} ='.format(n), end=' ')

        for i in range(len(factor) - 1):
            print('{} +'.format(factor[i]), end=' ')
        
        print(factor[-1])
    else:
        print('{} is NOT perfect.'.format(n))