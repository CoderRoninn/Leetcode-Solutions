class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums)-1

        while left <= right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                return middle
            if target > nums[middle]:
                left = middle +1
            else:
                right = middle -1
        return -1                

        