'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''


class Solution:
    def valid_palindrome(self, s: str) -> bool:
        output = True
        ckr: Deque = collections.deque()

        for c in s:
            if c.isalpha() or c.isdigit():
                ckr.append(c.lower())

        while len(ckr) > 1:
            if ckr.pop() == ckr.popleft():
                continue
            else:
                output = False
                
                return output

        return output