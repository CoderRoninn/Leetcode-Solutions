# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current, length = head, 0

        while current:
            length +=1
            current = current.next

        pointer1, pointer2 = head, head

        for _ in range(k-1):
            pointer1 = pointer1.next
        for _ in range(length - k):
            pointer2 = pointer2.next

        pointer1.val, pointer2.val = pointer2.val , pointer1.val
        
        return head     

        