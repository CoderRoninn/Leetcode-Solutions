class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)

        if len(nums) < 3:
            return max(nums)

        first = max(nums)
        nums.remove(first)
        second = max(nums)   
        nums.remove(second)
        third = max(nums)
        return third

        