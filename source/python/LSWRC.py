'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        str_set = []
        
        for idx, val in enumerate(s):
            if val in str_set:
                str_set = str_set[str_set.index(val) + 1:]
        
            str_set.append(val)
            output = max(output, len(str_set))
        
        return output