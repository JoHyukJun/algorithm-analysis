'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        ana = collections.defaultdict(list)
        
        for s in strs:
            ana[''.join(sorted(s))].append(s)
            
        output = ana.values()
        
        return output