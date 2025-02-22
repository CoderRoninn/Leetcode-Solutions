# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        link, slow, fast = None, head, head

        while fast and fast.next:
            link = slow
            slow = slow.next
            fast = fast.next.next

        link.next = link.next.next
        return head

   
        