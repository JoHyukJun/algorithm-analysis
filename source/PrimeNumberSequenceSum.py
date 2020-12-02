'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


import sys


n = int(sys.stdin.readline())

prime_number = []
answer = 0

temp_arr = [False, False] + [True] * (n - 1)

for i in range(2, n + 1):
    if temp_arr[i]:
        prime_number.append(i)
    
    for j in range(i * i, n + 1, i):
        temp_arr[j] = False

head = 0
tail = 0
temp = 0

while True:
    if temp >= n:
        if temp == n:
            answer += 1

        temp -= prime_number[head]
        head += 1
    elif tail == len(prime_number):
        break
    else:
        temp += prime_number[tail]
        tail += 1

print(answer)