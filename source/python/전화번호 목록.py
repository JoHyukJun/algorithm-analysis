'''

    main.py

    Created by Jo Hyuk Jun on 2022
    Copyright © 2022 Jo Hyuk Jun. All rights reserved.

'''


def solution(phone_book):
    answer = True
    
    if len(phone_book) <= 1:
        return answer
    
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if len(phone_book[i]) <= len(phone_book[j]):
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    answer = False
                    
                    return answer
    
    return answer