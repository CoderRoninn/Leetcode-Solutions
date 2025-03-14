import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        target = None

        while k > 0:
            target = -heapq.heappop(max_heap)
            k -= 1
        return target    
        