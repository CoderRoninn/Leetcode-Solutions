# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_nodes(head: Optional[ListNode]) -> Optional[ListNode]:

            prev, current = None, head
            while current:
                next_node = current.next
                current.next = prev

                prev = current
                current = next_node
            return prev
            
        new_head = reverse_nodes(head)

        current = new_head
        max_value = current.val

        while current and current.next:
            if max_value > current.next.val:
                current.next = current.next.next
            else:
                max_value = current.next.val
                current = current.next

        return reverse_nodes(new_head)

        