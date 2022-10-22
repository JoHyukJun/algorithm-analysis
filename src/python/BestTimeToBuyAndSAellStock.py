'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        m_price = sys.maxsize
        
        for p in prices:
            m_price = min(p, m_price)
            output = max(output, p - m_price)
            
        return output