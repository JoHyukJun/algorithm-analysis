'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seeker = {}
        
        for s in stones:
            if s in seeker:
                seeker[s] += 1
            else:
                seeker[s] = 1
                
        output = 0
        
        for j in jewels:
            if j in seeker:
                output += seeker[j]
        
        return output