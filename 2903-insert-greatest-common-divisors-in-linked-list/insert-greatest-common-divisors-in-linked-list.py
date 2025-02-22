# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a
        
        pointer1, pointer2 = head, head.next

        while pointer2:
            gcd_value = gcd(pointer1.val, pointer2.val)
            new_node = ListNode(gcd_value)
            pointer1.next = new_node
            new_node.next = pointer2
            pointer1 = pointer1.next.next
            pointer2 = pointer2.next
        return head    
                   
       

        