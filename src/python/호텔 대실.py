'''

    main.py

    Created by JO HYUK JUN on 2023
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(book_time):
    answer = 0
    
    for h in range(0, 25):
        for m in range(0, 61):
            cnt = 0
            for bt in book_time:
                start_h, start_m = map(int, bt[0].split(':'))
                end_h, end_m = map(int, bt[1].split(':'))
                
                end_m += 10
                end_m -= 1
                
                if (end_m > 60):
                    end_m %= 60
                    end_h += 1
                
                if (h == start_h and h == end_h):
                    if (m >= start_m and m <= end_m):
                        cnt += 1
                elif (h > start_h and h == end_h):
                    if (m <= end_m):
                        cnt += 1
                elif (h == start_h and h < end_h):
                    if (m >= start_m):
                        cnt += 1
                elif (h > start_h and h < end_h):
                    cnt += 1
                            
            if answer < cnt:
                answer = cnt
    
    return answer