'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        bias = 1
        
        for i in range(len(nums)):
            output.append(bias)
            bias *= nums[i]
            
        bias = 1
        
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= bias
            bias *= nums[i]
            
        return output