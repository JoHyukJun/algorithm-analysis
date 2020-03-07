'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        temp_list = []
        
        while head:
            temp_list.append(head.val)
            head = head.next
            
        swap_list = [0] * len(temp_list)
        
        remainder = len(temp_list) % k
        remainder = len(temp_list) - remainder
        
        for idx in range(0, len(temp_list)):
            div = idx // k
            pulse = div * k
            ckr = idx % k
            
            if (idx < remainder):
                swap_list[idx] = temp_list[pulse + k - 1 - ckr]
            else:
                swap_list[idx] = temp_list[idx]
                
        output = tail = ListNode(0)
        
        for idx in swap_list:
            tail.next = ListNode(idx)
            tail = tail.next
            
        return output.next