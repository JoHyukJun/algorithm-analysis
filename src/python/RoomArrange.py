'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())

time_list = []
answer = 0

for _ in range(n):
    time_list.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

time_list.sort(key=lambda x:x[0])
time_list.sort(key=lambda x:x[1])

end = 0

for tl in time_list:
    if tl[0] >= end:
        answer += 1
        end = tl[1]

print(answer)