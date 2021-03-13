'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


v = int(sys.stdin.readline())
votes = str(sys.stdin.readline().rstrip())

a = 0
b = 0

for i in range(len(votes)):
    if votes[i] == 'A':
        a += 1
    else:
        b += 1

if a > b:
    print('A')
elif a == b:
    print('Tie')
else:
    print('B')