'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        output = []
        dig = []
        let = []
        
        for v in logs:
            if v.split()[1].isdigit():
                dig.append(v)
            elif v.split()[1].isalpha():
                let.append(v)
                
        let.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        output = let + dig
        
        return output