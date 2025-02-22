# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        pointerF, pointerS = head, head

        while pointerF and pointerF.next:
            pointerS = pointerS.next
            pointerF = pointerF.next.next
        if pointerF:
            pointerS = pointerS.next

        current, prev = pointerS, None

        while current:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        left, right = head, prev

        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next

        return True 
        