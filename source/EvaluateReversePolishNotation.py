'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {'+', '-', '*', '/'}
        
        stack = []
        
        for token in tokens:
            if token in operator:
                x = int(stack.pop())
                y = int(stack.pop())
                
                if token == '+':
                    stack.append(y + x)
                elif token == '-':
                    stack.append(y - x)
                elif token == '*':
                    stack.append(y * x)
                elif token == '/':
                    stack.append(y / x)
            else:
                stack.append(int(token))
                
                
        return int(stack.pop())'