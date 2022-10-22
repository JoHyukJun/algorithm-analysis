'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''

import sys
from itertools import permutations

test_case_file = open(sys.argv[1], 'r')
sys.stdout = open('./result.txt', 'w')


def is_val(arg1, arg2):
    stack = []
    idx = 0

    for i in arg1:
        stack.append(i)

        while stack and stack[-1] == arg2[idx]:
            stack.pop()
            idx += 1

    return not stack


while (True):
    n = int(test_case_file.readline())
    
    if n == 0:
        break

    arr = [i for i in range(1, n + 1)]
    
    for i in (list(permutations(arr, n))):
        if (is_val(arr, list(i))):
            for j in i:
               print(j, end=' ')
            print()

    print()

test_case_file.close()
sys.stdout.close()import sys
from itertools import permutations

test_case_file = open(sys.argv[1], 'r')
sys.stdout = open('./result.txt', 'w')

while (True):
    n = int(test_case_file.readline())
    
    if n == 0:
        break

    arr = [i for i in range(1, n + 1)]
    
    for i in (list(permutations(arr, n))):
        for j in i:
            print(j, end=' ')

        print()

    print()

test_case_file.close()
sys.stdout.close()