# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        tail = head
        length = 1

        while tail.next:
            length += 1
            tail = tail.next

        tail.next = head    

        k = k % length

        if k == 0:
            tail.next = None
            return head

        current = head    
        for _ in range(length - k - 1):
            current = current.next
        new_head = current.next
        current.next =None    
        return new_head

        

        