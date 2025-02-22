# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        current, prev = head, None
        
        for _ in range(left - 1):
            prev = current
            current = current.next
            
        last_node_of_first_part = prev  
        first_node_of_reversed_list = current
        
        for i in range(right - left + 1):
            next_node = current.next
            current.next =prev
            
            prev = current
            current = next_node
        
        if last_node_of_first_part:
            last_node_of_first_part.next = prev
        else:
            head = prev
            
        first_node_of_reversed_list.next = current
        
        return head

        
            
        