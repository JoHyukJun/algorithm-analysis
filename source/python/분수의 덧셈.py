'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def gcd(x, y):
    while (y):
        x, y = y, x % y
        
    return x


def lcm(x, y):
    res = (x * y) // gcd(x, y)
    
    return res


def solution(denum1, num1, denum2, num2):
    answer = []
    co_num = lcm(num1, num2)
    answer = [denum1 * (co_num // num1) + denum2 * (co_num // num2), co_num]
    
    while (True):
        div = gcd(answer[0], answer[1])
        
        if (div == 1):
            break
        else:
            answer[0] //= div
            answer[1] //= div
            
    return answer