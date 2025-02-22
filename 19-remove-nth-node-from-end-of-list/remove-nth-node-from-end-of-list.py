# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        pointer1, pointer2 = head, head

        while n > 0 and pointer1:
            pointer1 = pointer1.next
            n -= 1

        if pointer1 is None:
            return head.next    

        while pointer1 and pointer1.next:
            pointer2 = pointer2.next
            pointer1 = pointer1.next

        
        pointer2.next = pointer2.next.next
        return head

       
        