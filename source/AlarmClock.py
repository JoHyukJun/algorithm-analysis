'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


h, m = map(int, sys.stdin.readline().rstrip().split(' '))

hour = 0
hour_carry = 0
minute = 0

if (m - 45 < 0):
    hour_carry -= 1
    minute = 60 + (m - 45)
else:
    minute = m - 45

if h + hour_carry < 0:
    hour = 24 + (h + hour_carry)
else:
    hour = h + hour_carry

print('{} {}'.format(hour, minute))