'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ''
        cnt = 0
        
        if len(s) == 0:
            return output
        
        for idx in range(0, len(s)):
            for iidx in range(idx + len(output), len(s) + 1):
                forward = s[idx:iidx]
                backward = forward[::-1]
                
                if forward == backward:
                    temp = forward
                    
                    if len(temp) > len(output):
                        output = temp
                        
        return output