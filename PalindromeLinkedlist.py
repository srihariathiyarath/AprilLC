# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        length = 0
        stack = []
        while node:
            stack.append(node.val)
            node = node.next
            length += 1
        
        node = head

        for item in stack[::-1]:
            if (item!= node.val):
                return False 
            node = node.next
        return True

        