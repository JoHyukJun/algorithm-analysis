'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


from math import gcd


def solution(dots):
    case1_a = [abs(dots[0][0] - dots[1][0]), abs(dots[0][1] - dots[1][1])]
    tmp_gcd = gcd(case1_a[0], case1_a[1])
    case1_a[0] //= tmp_gcd
    case1_a[1] //= tmp_gcd
    
    case1_b = [abs(dots[2][0] - dots[3][0]), abs(dots[2][1] - dots[3][1])]
    tmp_gcd = gcd(case1_b[0], case1_b[1])
    case1_b[0] //= tmp_gcd
    case1_b[1] //= tmp_gcd
    
    if case1_a == case1_b:
        return 1
    
    case2_a = [abs(dots[0][0] - dots[2][0]), abs(dots[0][1] - dots[2][1])]
    tmp_gcd = gcd(case2_a[0], case2_a[1])
    case2_a[0] //= tmp_gcd
    case2_a[1] //= tmp_gcd
    
    case2_b = [abs(dots[1][0] - dots[3][0]), abs(dots[1][1] - dots[3][1])]
    tmp_gcd = gcd(case2_b[0], case2_b[1])
    case2_b[0] //= tmp_gcd
    case2_b[1] //= tmp_gcd
    
    if case2_a == case2_b:
        return 1
    
    case3_a = [abs(dots[0][0] - dots[3][0]), abs(dots[0][1] - dots[3][1])]
    tmp_gcd = gcd(case3_a[0], case3_a[1])
    case3_a[0] //= tmp_gcd
    case3_a[1] //= tmp_gcd
    
    case3_b = [abs(dots[1][0] - dots[2][0]), abs(dots[1][1] - dots[2][1])]
    tmp_gcd = gcd(case3_b[0], case3_b[1])
    case3_b[0] //= tmp_gcd
    case3_b[1] //= tmp_gcd
    
    if case3_a == case3_b:
        return 1
            
    return 0