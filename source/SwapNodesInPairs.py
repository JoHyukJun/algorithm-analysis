'''

    main.py

    Created by Jo Hyuk Jun on 2020
    Copyright © 2020 Jo Hyuk Jun. All rights reserved.

'''


'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp_list = []
        
        while head:
            temp_list.append(head.val)
            head = head.next
            
        swap_list = [0] * len(temp_list)
        
        for idx in range(0, len(temp_list)):
            if (len(temp_list) % 2 == 0):
                if (idx % 2 == 0):
                    swap_list[idx + 1] = temp_list[idx]
                else:
                    swap_list[idx - 1] = temp_list[idx]
            else:
                if (idx == len(temp_list) - 1):
                    swap_list[idx] = temp_list[idx]
                    break
                
                if (idx % 2 == 0):
                    swap_list[idx + 1] = temp_list[idx]
                else:
                    swap_list[idx - 1] = temp_list[idx]
                    
        output = tail = ListNode(0)
        
        for idx in swap_list:
            tail.next = ListNode(idx)
            tail = tail.next
            
        return output.next