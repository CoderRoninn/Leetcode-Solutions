class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        
        sum = (n * (n+1)) // 2
        sum_array = 0

        for i in range(n):
            sum_array += nums[i]

        result = sum - sum_array

        return result    
        