'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        output = ''
        stack = []
        visited = set()
        cnt = collections.Counter(s)
        
        for c in s:
            cnt[c] -= 1
            
            if c in visited:
                continue
                
            while stack and c < stack[-1] and cnt[stack[-1]] > 0:
                visited.remove(stack.pop())
                
            stack.append(c)
            visited.add(c)
            
        output = ''.join(stack)
        
        return output