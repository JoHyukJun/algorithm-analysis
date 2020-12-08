'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


score = str(sys.stdin.readline().rstrip())

criteria = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
'F': 0.0}

print(criteria[score])