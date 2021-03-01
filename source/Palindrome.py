'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


word = str(sys.stdin.readline().rstrip())

half = len(word) // 2
carry = len(word) % 2

head = word[:half]
tail = word[half + carry:]

tail = tail[::-1]

if head == tail:
    print(1)
else:
    print(0)