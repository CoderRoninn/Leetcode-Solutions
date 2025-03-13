import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for (x,y) in points:
            distance = x * x + y * y
            min_heap.append([distance, x, y])

        result = []
        heapq.heapify(min_heap)

        while k > 0:
            distance, x, y = heapq.heappop(min_heap)
            result.append([x,y])  
            k -= 1
        return result     
        