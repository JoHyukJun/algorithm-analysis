'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        alpha_basis = 0
        beta_basis = 0
        head = 0
        tail = 0
        temp_set = set()
        ckr = 0
        
        if (len(nums) < 4):
            return output
        
        nums.sort()
        
        for alpha_basis in range (len(nums) - 2):
            for beta_basis in range(alpha_basis + 1, len(nums)):
                head = beta_basis + 1
                tail = len(nums) - 1
                ckr = target - nums[alpha_basis] - nums[beta_basis]
                
                while head < tail:
                    
                    if (ckr == nums[head] + nums[tail]):
                        temp_set.add((nums[alpha_basis],
                                    nums[beta_basis],
                                    nums[head],
                                    nums[tail]))
                        head += 1
                        tail -= 1
                    elif ckr < nums[head] + nums[tail]:
                        tail -= 1
                    else:
                        head += 1
                        
        output = list(temp_set)
        
        return output