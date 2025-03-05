# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        less_head, less = None, None
        greater_head, greater = None, None

        current = head

        while current:
            if current.val < x:
                if not less_head:
                    less_head = current
                    less = current
                else:
                    less.next = current
                    less = less.next
            else:
                if not greater_head:
                    greater_head = current
                    greater = current
                else:
                    greater.next = current
                    greater = greater.next 
            current = current.next

        if greater:
            greater.next = None
        if less:
            less.next = greater_head
            return less_head
        else:
            return greater_head    

        