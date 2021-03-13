'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


dishes = str(sys.stdin.readline().rstrip())
height = 10

for i in range(1, len(dishes)):
    if dishes[i] == dishes[i - 1]:
        height += 5
    else:
        height += 10

print(height)