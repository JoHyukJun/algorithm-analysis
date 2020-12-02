'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


eratos = [False, False] + [True] * (1000000)
prime_number = []

for i in range(2, 1000000):
    if eratos[i]:
        prime_number.append(i)
        
    for j in range(i * i, 1000000, i):
        eratos[j] = False


while True:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        break

    flag = True

    for i in range(3, 1000000):
        if eratos[i]:
            if eratos[n - i]:
                print('{} = {} + {}'.format(n, i, n - i))
                flag = False
                break

    if flag:
        print('Goldbach\'s conjecture is wrong.')

