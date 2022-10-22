'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())
word = []

for _ in range(n):
   word.append(str(sys.stdin.readline().rstrip()))

word = list(set(word))

length = [[] for _ in range(51)]

for i in range(len(word)):
    length[len(word[i])].append(word[i])

for i in range(len(length)):
    if (len(length[i]) == 0):
        continue
    elif (len(length[i]) == 1):
        print(length[i][0])
    else:
        s_len = sorted(length[i])

        for j in range(len(s_len)):
            print(s_len[j])