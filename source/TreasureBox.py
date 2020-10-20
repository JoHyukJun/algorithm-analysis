'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    output = 0

    n, k = map(int, input().split())
    l = str(input())

    tkey = list(l)
    basis = n // 4

    ckr_set = set()

    for i in range(basis):
        for j in range(4):
            head = j * basis
            tail = (j + 1) * basis

            #print(str(''.join(tkey[head:tail])))

            ckr_set.add(int(str(''.join(tkey[head:tail])), 16))

        tkey.insert(0, tkey[-1])
        tkey.pop()

    fin_l = []
    fin_l = list(ckr_set)

    fin_l.sort(reverse=True)


    print(fin_l)

    output = fin_l[k - 1]

    print(output)

