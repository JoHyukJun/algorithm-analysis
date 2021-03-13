'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


a, b = map(int, sys.stdin.readline().rstrip().split(' '))
c = int(sys.stdin.readline())

hour = 0
minute = 0
carry_hour = 0

if (b + c >= 60):
    carry_hour += (b + c) // 60
    minute = (b + c) % 60
else:
    minute = b + c

if (a + carry_hour >= 24):
    hour = (a + carry_hour) % 24
else:
    hour = a + carry_hour

print('{} {}'.format(hour, minute))