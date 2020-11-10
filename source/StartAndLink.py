'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys
from itertools import combinations


n = int(sys.stdin.readline())
arr = []
answer = sys.maxsize

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

members = [i for i in range(n)]
sel_num = n // 2
member_list = list(combinations(members, sel_num))

for i in range(len(member_list) // 2):
    start = list(member_list[i])
    link = list(set(i for i in range(n)) - set(start))
    s_point = 0
    l_point = 0
    for j in range(len(arr) // 2 - 1):
        for k in range(j + 1, len(arr[j]) // 2):
            s_point += arr[start[j]][start[k]] + arr[start[k]][start[j]]
            l_point += arr[link[j]][link[k]] + arr[link[k]][link[j]]
    
    temp = abs(s_point - l_point)
    if (answer > temp):
        answer = temp

print(answer)