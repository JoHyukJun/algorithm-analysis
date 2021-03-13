'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


score = int(sys.stdin.readline())

if score >= 90:
    print('A')
elif score >= 80 and score < 90:
    print('B')
elif score >= 70 and score < 80:
    print('C')
elif score >= 60 and score < 70:
    print('D')
else:
    print('F')