'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


a, b, c = map(int, sys.stdin.readline().rstrip().split(' '))
d = int(sys.stdin.readline())

hour = 0
minute = 0
second = 0
carry_minute = 0
carry_hour = 0

if (c + d >= 60):
    carry_minute += (c + d) // 60
    second = (c + d) % 60
else:
    second = c + d

if (b + carry_minute >= 60):
    carry_hour += (b + carry_minute) // 60
    minute = (b + carry_minute) % 60
else:
    minute = b + carry_minute

if (a + carry_hour >= 24):
    hour = (a + carry_hour) % 24
else:
    hour = a + carry_hour

print('{} {} {}'.format(hour, minute, second))