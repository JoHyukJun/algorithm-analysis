'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''


class Solution:
    def isValid(self, s: str) -> bool:
        output = True
        inputSize = len(s)
        ckrStack = []
        
        synDict = {'(': ')',
                  '{': '}',
                  '[': ']'}
        
        if (inputSize % 2 != 0):
            output = False
            return output
        
        for idx in range(0, inputSize):
            if s[idx] not in synDict.keys():
                if (len(ckrStack) == 0):
                    output = False
                    break
                
                if (s[idx] == ckrStack[len(ckrStack) - 1]):
                    ckrStack.pop()
                else:
                    output = False;
                    break
            else:
                ckrStack.append(synDict[s[idx]])
                
        if (len(ckrStack) != 0):
            output = False
                
        return output